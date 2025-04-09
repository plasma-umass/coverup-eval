# file: tornado/escape.py:59-61
# asked: {"lines": [59, 61], "branches": []}
# gained: {"lines": [59, 61], "branches": []}

import pytest
import re
from tornado.escape import xhtml_unescape

def _convert_entity(m):
    if m.group(1) == "#":
        try:
            if m.group(2)[:1].lower() == 'x':
                return chr(int(m.group(2)[1:], 16))
            else:
                return chr(int(m.group(2)))
        except ValueError:
            return m.group(0)
    else:
        try:
            return html.entities.name2codepoint[m.group(2)]
        except KeyError:
            return m.group(0)

def _unicode(value):
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value

@pytest.mark.parametrize("input_str, expected_output", [
    ("&lt;div&gt;", "<div>"),
    ("&amp;#x27;", "&#x27;"),
    ("&amp;#39;", "&#39;"),
    ("&amp;#x3C;", "&#x3C;"),
    ("&amp;#60;", "&#60;"),
    ("&amp;#x3E;", "&#x3E;"),
    ("&amp;#62;", "&#62;"),
    ("&amp;#x26;", "&#x26;"),
    ("&amp;#38;", "&#38;"),
    ("&amp;#x22;", "&#x22;"),
    ("&amp;#34;", "&#34;"),
    ("&amp;#x27;", "&#x27;"),
    ("&amp;#39;", "&#39;"),
    ("&amp;#x3C;", "&#x3C;"),
    ("&amp;#60;", "&#60;"),
    ("&amp;#x3E;", "&#x3E;"),
    ("&amp;#62;", "&#62;"),
    ("&amp;#x26;", "&#x26;"),
    ("&amp;#38;", "&#38;"),
    ("&amp;#x22;", "&#x22;"),
    ("&amp;#34;", "&#34;"),
    ("&amp;#x27;", "&#x27;"),
    ("&amp;#39;", "&#39;"),
    ("&amp;#x3C;", "&#x3C;"),
    ("&amp;#60;", "&#60;"),
    ("&amp;#x3E;", "&#x3E;"),
    ("&amp;#62;", "&#62;"),
    ("&amp;#x26;", "&#x26;"),
    ("&amp;#38;", "&#38;"),
    ("&amp;#x22;", "&#x22;"),
    ("&amp;#34;", "&#34;"),
])
def test_xhtml_unescape(input_str, expected_output):
    assert xhtml_unescape(input_str) == expected_output
