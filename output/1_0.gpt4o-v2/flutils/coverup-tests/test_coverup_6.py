# file: flutils/strutils.py:157-209
# asked: {"lines": [157, 205, 206, 207, 208, 209], "branches": []}
# gained: {"lines": [157, 205, 206, 207, 208, 209], "branches": []}

import pytest
from flutils.strutils import convert_escaped_utf8_literal

def test_convert_escaped_utf8_literal_basic():
    input_str = 'test\\xc2\\xa9'
    expected_output = 'test©'
    assert convert_escaped_utf8_literal(input_str) == expected_output

def test_convert_escaped_utf8_literal_unicode_error():
    input_str = 'test\\xc2\\xa9\\xc3'
    with pytest.raises(UnicodeDecodeError):
        convert_escaped_utf8_literal(input_str)

def test_convert_escaped_utf8_literal_empty_string():
    input_str = ''
    expected_output = ''
    assert convert_escaped_utf8_literal(input_str) == expected_output

def test_convert_escaped_utf8_literal_no_escapes():
    input_str = 'test'
    expected_output = 'test'
    assert convert_escaped_utf8_literal(input_str) == expected_output

def test_convert_escaped_utf8_literal_multiple_escapes():
    input_str = 'test\\xc2\\xa9 and \\xc3\\xb1'
    expected_output = 'test© and ñ'
    assert convert_escaped_utf8_literal(input_str) == expected_output
