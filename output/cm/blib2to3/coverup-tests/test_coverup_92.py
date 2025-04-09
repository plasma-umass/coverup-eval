# file src/blib2to3/pgen2/literals.py:47-55
# lines [51]
# branches ['50->51']

import pytest
from blib2to3.pgen2.literals import evalString

def test_evalString_triple_quotes():
    # Test with triple single quotes
    input_str = "'''abc'''"
    expected = "abc"
    assert evalString(input_str) == expected

    # Test with triple double quotes
    input_str = '"""abc"""'
    expected = "abc"
    assert evalString(input_str) == expected

def test_evalString_single_quotes():
    # Test with single quotes
    input_str = "'abc'"
    expected = "abc"
    assert evalString(input_str) == expected

def test_evalString_double_quotes():
    # Test with double quotes
    input_str = '"abc"'
    expected = "abc"
    assert evalString(input_str) == expected

def test_evalString_escaped_characters():
    # Test with escaped characters
    input_str = r"'a\\nb\\tc'"
    expected = "a\\nb\\tc"
    assert evalString(input_str) == expected

def test_evalString_hex_escape():
    # Test with hex escape
    input_str = r"'\x61\x62\x63'"
    expected = "abc"
    assert evalString(input_str) == expected

def test_evalString_octal_escape():
    # Test with octal escape
    input_str = r"'\141\142\143'"
    expected = "abc"
    assert evalString(input_str) == expected

def test_evalString_invalid():
    # Test with invalid string
    with pytest.raises(AssertionError):
        evalString('abc')

def test_evalString_empty():
    # Test with empty string
    with pytest.raises(AssertionError):
        evalString('')

def test_evalString_unmatched_quotes():
    # Test with unmatched quotes
    with pytest.raises(AssertionError):
        evalString("'abc\"")
