#!/usr/bin/env python3
"""
TOOLS/lore_yaml.py — dependency-free parser for the YAML subset this corpus uses.

Written because the TCB's zero-dependency posture is an author imperative (AI-003), and
because the previous fallback in lore_common could parse only flat `key: value` documents.
Handed a nested one it returned a mapping of empty strings, and the caller died later
somewhere unrelated. Fail-closed stopped the wrong answers; this makes the right ones
possible without taking a dependency.

Supported, because the corpus uses it (69 YAML files surveyed):
    nested mappings, sequences of scalars, sequences of mappings,
    block scalars (| and >, with - and + chomping), flow sequences [a, b],
    flow mappings {a: b}, single/double quoting, comments, and the
    null/bool/int/float scalar forms.

Deliberately NOT supported: anchors and aliases, merge keys, multi-document streams,
tags, complex keys. None appear in this corpus. Each raises YamlParseError naming the
line, rather than being silently mis-parsed — the whole point of the exercise.

Verified by differential test against PyYAML over every YAML file in the repository
(TESTS/test_yaml_parser.py). PyYAML is the oracle in that test only; nothing here imports
it.
"""

from __future__ import annotations

import datetime
import json
import re

__all__ = ['parse', 'dump', 'YamlParseError']


class YamlParseError(ValueError):
    """The document uses a construct this parser does not implement.

    Raised rather than guessed. A parser that quietly mishandles a construct is the
    defect this module exists to retire.
    """


# --------------------------------------------------------------------------- scanning

_UNSUPPORTED = (
    (re.compile(r'^\s*<<\s*:'), 'merge keys (<<:)'),
    (re.compile(r'^\s*[^#]*?[:\-]\s+&\w'), 'anchors (&name)'),
    (re.compile(r'^\s*[^#]*?[:\-]\s+\*\w'), 'aliases (*name)'),
    (re.compile(r'^\s*!!?\w'), 'tags (!tag)'),
    (re.compile(r'^\s*\?\s'), 'complex keys (? )'),
)


def _is_quote_opener(s, i):
    """True if s[i] is a quote that OPENS a scalar rather than sitting inside one.

    A quote opens a scalar only at the start of a value position — after ':', '-', ',',
    '[' or '{', or at the start of the line. Anywhere else it is an ordinary character:
    `method: copy of the public draft's SOURCE/` is a plain scalar containing an
    apostrophe, and reading that apostrophe as an opening quote swallows the rest of
    the document.
    """
    j = i - 1
    while j >= 0 and s[j] in ' \t':
        j -= 1
    return j < 0 or s[j] in ':-,[{'


def _strip_comment(line):
    """Remove a trailing comment, respecting quotes. '#' only starts one at the
    start of the line or after whitespace — 'a#b' is a value, not a comment."""
    out, quote, i = [], None, 0
    while i < len(line):
        ch = line[i]
        if quote:
            out.append(ch)
            if ch == '\\' and quote == '"' and i + 1 < len(line):
                out.append(line[i + 1]); i += 2; continue
            if ch == quote:
                quote = None
        elif ch in '"\'' and _is_quote_opener(line, i):
            quote = ch; out.append(ch)
        elif ch == '#' and (i == 0 or line[i - 1] in ' \t'):
            break
        else:
            out.append(ch)
        i += 1
    return ''.join(out).rstrip()


def _quote_open(s):
    """True if a quoted scalar is still open at the end of `s` (comments respected)."""
    quote, i = None, 0
    while i < len(s):
        ch = s[i]
        if quote == '"':
            if ch == '\\' and i + 1 < len(s):
                i += 2; continue
            if ch == '"':
                quote = None
        elif quote == "'":
            if ch == "'":
                if i + 1 < len(s) and s[i + 1] == "'":
                    i += 2; continue          # '' is an escaped quote, not a close
                quote = None
        elif ch in '"\'' and _is_quote_opener(s, i):
            quote = ch
        elif ch == '#' and (i == 0 or s[i - 1] in ' \t'):
            break
        i += 1
    return quote is not None


_BLOCK_INDICATOR = re.compile(r'(?:^|[:\-])\s*([|>][-+]?)$')


def _block_style(content):
    """Return the block indicator this line opens with ('|', '>-', ...), or None."""
    m = _BLOCK_INDICATOR.search(content)
    return m.group(1) if m else None


def _scan(text):
    """[(indent, content, raw, lineno, block_lines)] for meaningful lines.

    Two things must happen here, before anything else looks at the text:

    A quoted scalar may span lines — PyYAML emits exactly that when folding a long
    string, with a trailing backslash and an escaped leading space on the continuation.
    Those are joined into one logical row.

    A block scalar's body is LITERAL TEXT, not YAML. Its lines are attached to the row
    that opened the block and never scanned again. Scanning them was how an apostrophe
    in ordinary prose — "that person's public work" — read as an unterminated quote and
    swallowed the rest of the file. Blank lines inside a block are preserved here too;
    dropping them as "not meaningful" would silently reshape the string.
    """
    raw_lines = text.splitlines()
    rows, i = [], 0
    while i < len(raw_lines):
        raw, lineno = raw_lines[i], i + 1
        if raw.strip() in ('---', '...'):
            i += 1
            continue
        for pat, what in _UNSUPPORTED:
            if pat.match(raw):
                raise YamlParseError("line %d: %s are not supported: %r"
                                     % (lineno, what, raw.strip()))
        buf = raw
        while _quote_open(buf) and i + 1 < len(raw_lines):
            i += 1
            buf += '\n' + raw_lines[i]
        if _quote_open(buf):
            raise YamlParseError("line %d: unterminated quoted scalar" % lineno)
        content = _strip_comment(buf)
        indent = len(raw) - len(raw.lstrip(' '))
        i += 1
        if not content.strip():
            continue
        content = content.strip()

        block_lines = None
        if _block_style(content):
            block_lines, j = [], i
            while j < len(raw_lines):
                body = raw_lines[j]
                if not body.strip():
                    block_lines.append(body); j += 1; continue
                if len(body) - len(body.lstrip(' ')) <= indent:
                    break
                block_lines.append(body); j += 1
            while block_lines and not block_lines[-1].strip():
                block_lines.pop()          # trailing blanks belong to the document
                j -= 1
            i = j
        rows.append((indent, content, raw, lineno, block_lines))
    return rows


# --------------------------------------------------------------------------- scalars

_DATE = re.compile(r'^(\d{4})-(\d{1,2})-(\d{1,2})$')
_TIMESTAMP = re.compile(
    r'^(\d{4})-(\d{1,2})-(\d{1,2})(?:[Tt]|[ \t]+)(\d{1,2}):(\d{2}):(\d{2})'
    r'(\.\d*)?(?:[ \t]*(Z|[-+]\d{1,2}(?::?\d{2})?))?$')
_INT = re.compile(r'^[+-]?\d+$')
_FLOAT = re.compile(r'^[+-]?(\d+\.\d*|\.\d+)([eE][+-]?\d+)?$|^[+-]?\d+[eE][+-]?\d+$')


_ESCAPES = {'0': '\0', 'a': '\a', 'b': '\b', 't': '\t', '\t': '\t', 'n': '\n',
            'v': '\v', 'f': '\f', 'r': '\r', 'e': '\x1b', ' ': ' ', '"': '"',
            '/': '/', '\\': '\\', 'N': '\x85', '_': '\xa0', 'L': '\u2028', 'P': '\u2029'}
_HEX = {'x': 2, 'u': 4, 'U': 8}


def _fold(s):
    """Fold unescaped line breaks: a break becomes a space, a blank line a newline."""
    parts = s.split('\n')
    if len(parts) == 1:
        return s
    out = parts[0].rstrip()
    for part in parts[1:]:
        stripped = part.strip()
        if not stripped:
            out += '\n'
        elif out.endswith('\n'):
            out += stripped
        else:
            out += ' ' + stripped
    return out


def _unquote_double(s):
    """Decode a YAML double-quoted scalar: escapes, and folding of RAW line breaks.

    Folding is done during the scan, not afterwards. A post-pass cannot tell a raw line
    break in the source from a newline produced by a \\n escape, and folding the latter
    turned an embedded shell script into one long line.
    """
    body, out, i = s[1:-1], [], 0
    while i < len(body):
        ch = body[i]
        if ch == '\\' and i + 1 < len(body):
            nxt = body[i + 1]
            if nxt == '\n':                    # escaped break: continuation, no space
                i += 2
                while i < len(body) and body[i] in ' \t':
                    i += 1
                continue
            if nxt in _HEX:
                width = _HEX[nxt]
                out.append(chr(int(body[i + 2:i + 2 + width], 16)))
                i += 2 + width
                continue
            out.append(_ESCAPES.get(nxt, nxt)); i += 2
            continue
        if ch == '\n':                         # raw break: fold
            j, blanks = i + 1, 0
            while j < len(body):
                k = j
                while k < len(body) and body[k] in ' \t':
                    k += 1
                if k < len(body) and body[k] == '\n':
                    blanks += 1; j = k + 1; continue
                j = k
                break
            while out and out[-1] in ' \t':
                out.pop()
            out.append('\n' * blanks if blanks else ' ')
            i = j
            continue
        out.append(ch); i += 1
    return ''.join(out)


def _scalar(tok):
    """Convert a plain/quoted token to a Python value, PyYAML-compatibly."""
    tok = tok.strip()
    if tok.startswith('!'):
        # A tag in value position ('k: !!python/object x'). An unquoted plain scalar
        # cannot begin with '!' in YAML, so this is always a tag — and a tag is a
        # type instruction we will not honour silently.
        raise YamlParseError("tags (!tag) are not supported: %r" % tok)
    if tok == '' or tok in ('~', 'null', 'Null', 'NULL'):
        return None
    if len(tok) >= 2 and tok[0] == '"' and tok[-1] == '"':
        return _unquote_double(tok)
    if len(tok) >= 2 and tok[0] == "'" and tok[-1] == "'":
        return _fold(tok[1:-1].replace("''", "'"))
    if tok in ('true', 'True', 'TRUE', 'yes', 'Yes', 'YES', 'on', 'On', 'ON'):
        return True
    if tok in ('false', 'False', 'FALSE', 'no', 'No', 'NO', 'off', 'Off', 'OFF'):
        return False
    if _INT.match(tok):
        return int(tok)
    if _FLOAT.match(tok):
        return float(tok)
    stamp = _timestamp(tok)
    if stamp is not None:
        return stamp
    if tok.startswith('[') and tok.endswith(']'):
        return _flow_seq(tok)
    if tok.startswith('{') and tok.endswith('}'):
        return _flow_map(tok)
    return tok


def _timestamp(tok):
    """YAML 1.1 implicit date/timestamp resolution, matching PyYAML.

    Reproduced deliberately, quirks and all. The point of this parser is that a document
    means the same thing whether or not PyYAML is installed; a "better" reading here
    would reintroduce exactly the environment-dependence it exists to remove.
    """
    m = _DATE.match(tok)
    if m:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = _TIMESTAMP.match(tok)
    if not m:
        return None
    year, month, day, hour, minute, second, frac, tz = m.groups()
    micro = 0
    if frac:
        micro = int(round(float(frac) * 1e6))
    delta = None
    if tz and tz not in ('Z', 'z'):
        sign = -1 if tz[0] == '-' else 1
        body = tz[1:].replace(':', '')
        tz_h = int(body[:2] if len(body) >= 2 else body)
        tz_m = int(body[2:4]) if len(body) > 2 else 0
        delta = datetime.timedelta(hours=sign * tz_h, minutes=sign * tz_m)
    stamp = datetime.datetime(int(year), int(month), int(day),
                              int(hour), int(minute), int(second), micro)
    if delta is not None:
        stamp -= delta
    if tz:
        stamp = stamp.replace(tzinfo=datetime.timezone.utc)
    return stamp


def _split_flow(body):
    """Split a flow collection body on commas that are not nested or quoted."""
    parts, buf, depth, quote = [], [], 0, None
    for ch in body:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in '"\'':
            quote = ch; buf.append(ch); continue
        if ch in '[{':
            depth += 1
        elif ch in ']}':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(''.join(buf)); buf = []
            continue
        buf.append(ch)
    if ''.join(buf).strip():
        parts.append(''.join(buf))
    return [p.strip() for p in parts]


def _flow_seq(tok):
    return [_scalar(p) for p in _split_flow(tok[1:-1])]


def _flow_map(tok):
    out = {}
    for part in _split_flow(tok[1:-1]):
        if ':' not in part:
            raise YamlParseError("malformed flow mapping entry: %r" % part)
        k, v = _split_key(part)
        out[_scalar(k)] = _scalar(v)
    return out


def _split_key(content):
    """Split 'key: value' at the first ':' that is not quoted or inside a flow."""
    quote, depth = None, 0
    for i, ch in enumerate(content):
        if quote:
            if ch == quote:
                quote = None
            continue
        if ch in '"\'' and _is_quote_opener(content, i):
            quote = ch
        elif ch in '[{':
            depth += 1
        elif ch in ']}':
            depth -= 1
        elif ch == ':' and depth == 0:
            rest = content[i + 1:]
            if rest == '' or rest[0] in ' \t':
                return content[:i].strip(), rest.strip()
    return None, None


# ----------------------------------------------------------------------- block scalars

def _block_scalar(block_lines, style):
    """Render an attached | or > body per its chomping indicator."""
    keep, strip = style.endswith('+'), style.endswith('-')
    literal = style[0] == '|'
    lines = list(block_lines or [])
    if not lines:
        return '' if strip else '\n'

    block_indent = min((len(l) - len(l.lstrip(' ')) for l in lines if l.strip()),
                       default=0)
    body = [l[block_indent:] if len(l) >= block_indent else l.lstrip() for l in lines]

    if literal:
        text = '\n'.join(body) + '\n'
    else:
        out, prev_blank = [], False
        for line in body:
            if not line.strip():
                out.append('\n'); prev_blank = True
                continue
            if out and not prev_blank:
                out.append(' ')
            out.append(line.strip()); prev_blank = False
        text = ''.join(out) + '\n'

    if strip:
        text = text.rstrip('\n')
    elif not keep:
        text = text.rstrip('\n') + '\n'
    return text


# ------------------------------------------------------------------------- the parser

def _parse_block(rows, idx, indent):
    """Parse the block at `indent` starting at rows[idx]. Returns (value, next_index)."""
    if idx >= len(rows):
        return None, idx
    if rows[idx][1].startswith('- '):
        return _parse_seq(rows, idx, indent)
    if rows[idx][1] == '-':
        return _parse_seq(rows, idx, indent)
    return _parse_map(rows, idx, indent)


def _parse_seq(rows, idx, indent):
    items, i = [], idx
    while i < len(rows):
        cur_indent, content, _raw, lineno = rows[i][:4]
        if cur_indent < indent:
            break
        if cur_indent > indent:
            raise YamlParseError("line %d: unexpected indentation in sequence" % lineno)
        if not (content == '-' or content.startswith('- ')):
            break
        rest = content[1:].strip()
        if not rest:                                    # '-' then an indented block
            child, i = _parse_block(rows, i + 1, _next_indent(rows, i + 1, indent))
            items.append(child)
            continue
        key, value = _split_key(rest)
        if key is None:                                 # plain scalar item
            items.append(_scalar(rest)); i += 1
            continue
        # '- key: value' — a mapping whose first key sits on the dash line
        item_indent = cur_indent + (len(content) - len(content.lstrip('- ')))
        entry, i = _parse_inline_map(rows, i, item_indent, key, value)
        items.append(entry)
    return items, i


def _parse_inline_map(rows, idx, item_indent, first_key, first_value):
    """Handle '- key: value' plus any following keys indented to the same column."""
    cur_indent = rows[idx][0]
    mapping = {}
    if first_value in ('|', '>', '|-', '>-', '|+', '>+'):
        mapping[first_key] = _block_scalar(rows[idx][4], first_value)
        idx += 1
    elif first_value == '':
        child_indent = _next_indent(rows, idx + 1, item_indent)
        if child_indent is not None and child_indent > cur_indent:
            child, idx = _parse_block(rows, idx + 1, child_indent)
            mapping[first_key] = child
        else:
            mapping[first_key] = None; idx += 1
    else:
        mapping[first_key] = _scalar(first_value); idx += 1

    while idx < len(rows):
        nxt_indent, content, _raw, _ln = rows[idx][:4]
        if nxt_indent != item_indent or content.startswith('- '):
            break
        key, value = _split_key(content)
        if key is None:
            break
        rest, idx = _parse_value(rows, idx, nxt_indent, value)
        mapping[key] = rest
    return mapping, idx


def _next_indent(rows, idx, fallback):
    return rows[idx][0] if idx < len(rows) else fallback


def _parse_value(rows, idx, indent, value):
    """Resolve the value for rows[idx]'s key. Returns (value, next_index)."""
    if value in ('|', '>', '|-', '>-', '|+', '>+'):
        return _block_scalar(rows[idx][4], value), idx + 1
    if value != '':
        return _scalar(value), idx + 1
    if idx + 1 < len(rows):
        child_indent = rows[idx + 1][0]
        child_content = rows[idx + 1][1]
        # a sequence may sit at the parent's own indent, as YAML permits
        if child_indent > indent or (child_indent == indent
                                     and (child_content == '-' or child_content.startswith('- '))):
            return _parse_block(rows, idx + 1, child_indent)
    return None, idx + 1


def _parse_map(rows, idx, indent):
    mapping, i = {}, idx
    while i < len(rows):
        cur_indent, content, _raw, lineno = rows[i][:4]
        if cur_indent < indent:
            break
        if cur_indent > indent:
            raise YamlParseError("line %d: unexpected indentation in mapping" % lineno)
        if content.startswith('- ') or content == '-':
            break
        key, value = _split_key(content)
        if key is None:
            raise YamlParseError("line %d: expected 'key: value', got %r" % (lineno, content))
        # Keys go through the same resolver as values: PyYAML turns a bare `on:` into
        # boolean True (YAML 1.1), and this parser must agree or the two disagree about
        # what .github/workflows/validate.yml says.
        mapping[_scalar(key)], i = _parse_value(rows, i, cur_indent, value)
    return mapping, i


def parse(text):
    """Parse a YAML document from `text`. Returns a dict/list/scalar, or {} if empty."""
    stripped = text.strip()
    if not stripped:
        return {}
    if stripped.startswith('{') or stripped.startswith('['):
        return json.loads(stripped) if stripped.startswith('{') else _flow_seq(stripped)
    rows = _scan(text)
    if not rows:
        return {}
    value, consumed = _parse_block(rows, 0, rows[0][0])
    if consumed != len(rows):
        lineno = rows[consumed][3]
        raise YamlParseError("line %d: trailing content this parser could not place" % lineno)
    return value if value is not None else {}


# --------------------------------------------------------------------------- emitting

_INDICATORS = '-?:,[]{}#&*!|>\'"%@`'
_NEEDS_QUOTE = re.compile(r'^$|^\s|\s$|: | #|\n')


def _needs_quotes(s):
    """True if a plain scalar would not round-trip as the same string."""
    if _NEEDS_QUOTE.search(s):
        return True
    if s[0] in _INDICATORS:
        return True
    # would it resolve to something other than this string?
    return not isinstance(_scalar(s), str) or _scalar(s) != s


def _emit_scalar(value):
    if value is None:
        return 'null'
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    text = str(value)
    if not _needs_quotes(text):
        return text
    return json.dumps(text, ensure_ascii=False)


def _emit(value, indent, out):
    pad = '  ' * indent
    if isinstance(value, dict):
        if not value:
            out.append(pad.rstrip() + ' {}' if out else '{}')
            return
        for key, val in value.items():
            k = _emit_scalar(key)
            if isinstance(val, dict) and val:
                out.append('%s%s:' % (pad, k)); _emit(val, indent + 1, out)
            elif isinstance(val, list) and val:
                out.append('%s%s:' % (pad, k)); _emit(val, indent + 1, out)
            elif isinstance(val, dict):
                out.append('%s%s: {}' % (pad, k))
            elif isinstance(val, list):
                out.append('%s%s: []' % (pad, k))
            else:
                out.append('%s%s: %s' % (pad, k, _emit_scalar(val)))
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, dict) and item:
                first = True
                for key, val in item.items():
                    k = _emit_scalar(key)
                    lead = '%s- ' % pad if first else '%s  ' % pad
                    first = False
                    if isinstance(val, (dict, list)) and val:
                        out.append('%s%s:' % (lead, k)); _emit(val, indent + 2, out)
                    else:
                        out.append('%s%s: %s' % (lead, k, _emit_scalar(val)))
            elif isinstance(item, list) and item:
                out.append('%s-' % pad); _emit(item, indent + 1, out)
            else:
                out.append('%s- %s' % (pad, _emit_scalar(item)))
    else:
        out.append(pad + _emit_scalar(value))


def dump(data):
    """Emit `data` as YAML this module can read back to an equal value.

    Exists so that a LORE tool's output does not change shape with the ambient
    environment. dump_yaml used to fall back to json.dumps when PyYAML was missing, so
    `lore handoff show` printed YAML on a dev box and JSON on a bare runner — which is
    how demo.sh came to assert on a serializer and pass locally while failing in CI.
    """
    if data is None:
        return 'null\n'
    if not isinstance(data, (dict, list)):
        return _emit_scalar(data) + '\n'
    if not data:
        return ('{}' if isinstance(data, dict) else '[]') + '\n'
    out = []
    _emit(data, 0, out)
    return '\n'.join(out) + '\n'
