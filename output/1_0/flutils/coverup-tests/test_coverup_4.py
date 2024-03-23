# file flutils/strutils.py:100-154
# lines [100, 153, 154]
# branches []

import pytest
from flutils.strutils import convert_escaped_unicode_literal

def test_convert_escaped_unicode_literal():
    # Test with a string containing various escaped unicode literals
    input_str = '\\x31\\x2e\\u2605\\x20\\U0001f6d1'
    expected_output = '1.★ 🛑'
    assert convert_escaped_unicode_literal(input_str) == expected_output

    # Test with a string containing no escaped unicode literals
    input_str_no_escape = 'Test string with no escape'
    expected_output_no_escape = 'Test string with no escape'
    assert convert_escaped_unicode_literal(input_str_no_escape) == expected_output_no_escape

    # Test with a string containing only escaped unicode literals
    input_str_only_escape = '\\x31\\u0031\\U00000031'
    expected_output_only_escape = '111'
    assert convert_escaped_unicode_literal(input_str_only_escape) == expected_output_only_escape

    # Test with an empty string
    input_str_empty = ''
    expected_output_empty = ''
    assert convert_escaped_unicode_literal(input_str_empty) == expected_output_empty
