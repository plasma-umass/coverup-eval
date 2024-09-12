# file: flutils/strutils.py:13-44
# asked: {"lines": [13, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44], "branches": [[35, 36], [35, 44], [38, 39], [38, 40], [40, 41], [40, 43]]}
# gained: {"lines": [13, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44], "branches": [[35, 36], [35, 44], [38, 39], [38, 40], [40, 41], [40, 43]]}

import pytest
from flutils.strutils import as_escaped_unicode_literal

def test_as_escaped_unicode_literal():
    # Test with a mix of characters to cover all branches
    text = '1.★ 🛑'
    expected_output = '\\x31\\x2e\\u2605\\x20\\U0001f6d1'
    assert as_escaped_unicode_literal(text) == expected_output

    # Test with single character that results in \x escape
    text = 'A'
    expected_output = '\\x41'
    assert as_escaped_unicode_literal(text) == expected_output

    # Test with single character that results in \u escape
    text = '★'
    expected_output = '\\u2605'
    assert as_escaped_unicode_literal(text) == expected_output

    # Test with single character that results in \U escape
    text = '🛑'
    expected_output = '\\U0001f6d1'
    assert as_escaped_unicode_literal(text) == expected_output

    # Test with empty string
    text = ''
    expected_output = ''
    assert as_escaped_unicode_literal(text) == expected_output
