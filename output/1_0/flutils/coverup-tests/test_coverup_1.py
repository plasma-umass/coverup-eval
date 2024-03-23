# file flutils/strutils.py:13-44
# lines [13, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44]
# branches ['35->36', '35->44', '38->39', '38->40', '40->41', '40->43']

import pytest
from flutils.strutils import as_escaped_unicode_literal

def test_as_escaped_unicode_literal():
    # Test with characters that have different lengths when converted to hex
    text = 'a\u00e9\u20ac\U0001f600'  # a, é, €, 😀
    expected = '\\x61\\xe9\\u20ac\\U0001f600'
    assert as_escaped_unicode_literal(text) == expected

    # Test with empty string
    assert as_escaped_unicode_literal('') == ''

    # Test with single character
    assert as_escaped_unicode_literal('a') == '\\x61'

    # Test with character that will be converted to 3 hex digits
    assert as_escaped_unicode_literal('\u0100') == '\\u0100'

    # Test with character that will be converted to 5 hex digits
    assert as_escaped_unicode_literal('\U00010000') == '\\U00010000'
