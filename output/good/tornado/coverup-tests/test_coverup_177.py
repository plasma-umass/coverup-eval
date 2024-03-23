# file tornado/escape.py:59-61
# lines [59, 61]
# branches []

import pytest
from tornado.escape import xhtml_unescape

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup if necessary after tests
    yield
    # Here you can put any cleanup code if needed, but for this test, it seems unnecessary.

def _convert_entity(m):
    if m.group(1) == "#":
        try:
            if m.group(2)[0].lower() == "x":
                return chr(int(m.group(2)[1:], 16))
            else:
                return chr(int(m.group(2)))
        except ValueError:
            return "&#%s;" % m.group(2)
    try:
        return chr(html.entities.name2codepoint[m.group(2)])
    except KeyError:
        return "&%s;" % m.group(2)

def test_xhtml_unescape_numeric_entity(cleanup):
    # Test numeric character reference
    assert xhtml_unescape("&#34;") == '"', "Numeric entity not unescaped correctly"

def test_xhtml_unescape_hex_entity(cleanup):
    # Test hexadecimal character reference
    assert xhtml_unescape("&#x22;") == '"', "Hexadecimal entity not unescaped correctly"

def test_xhtml_unescape_named_entity(cleanup):
    # Test named character reference
    assert xhtml_unescape("&quot;") == '"', "Named entity not unescaped correctly"

def test_xhtml_unescape_invalid_numeric_entity(cleanup):
    # Test invalid numeric character reference
    assert xhtml_unescape("&#34") == "&#34", "Invalid numeric entity should not be unescaped"

def test_xhtml_unescape_invalid_hex_entity(cleanup):
    # Test invalid hexadecimal character reference
    assert xhtml_unescape("&#x22") == "&#x22", "Invalid hexadecimal entity should not be unescaped"

def test_xhtml_unescape_invalid_named_entity(cleanup):
    # Test invalid named character reference
    assert xhtml_unescape("&unknown;") == "&unknown;", "Invalid named entity should not be unescaped"
