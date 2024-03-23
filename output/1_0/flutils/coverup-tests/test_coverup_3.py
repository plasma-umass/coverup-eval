# file flutils/strutils.py:157-209
# lines [157, 205, 206, 207, 208, 209]
# branches []

import pytest
from flutils.strutils import convert_escaped_utf8_literal

def test_convert_escaped_utf8_literal():
    # Test with a string containing escaped UTF-8 hexadecimal characters
    input_str = 'test\\xc2\\xa9'
    expected_output = 'test©'
    assert convert_escaped_utf8_literal(input_str) == expected_output

    # Test with a string that does not contain escaped characters
    input_str_no_escape = 'test'
    expected_output_no_escape = 'test'
    assert convert_escaped_utf8_literal(input_str_no_escape) == expected_output_no_escape

    # Test with a string that contains invalid UTF-8 escape sequences
    input_str_invalid = 'test\\xc3\\x28'
    with pytest.raises(UnicodeDecodeError):
        convert_escaped_utf8_literal(input_str_invalid)
