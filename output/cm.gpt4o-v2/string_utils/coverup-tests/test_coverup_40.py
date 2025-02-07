# file: string_utils/manipulation.py:611-634
# asked: {"lines": [611, 634], "branches": []}
# gained: {"lines": [611, 634], "branches": []}

import pytest
from string_utils.manipulation import roman_encode

def test_roman_encode_integer():
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(2020) == 'MMXX'

def test_roman_encode_string():
    assert roman_encode('37') == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'

def test_roman_encode_invalid_input():
    with pytest.raises(ValueError, match='Invalid input, only strings or integers are allowed'):
        roman_encode(3.5)
    with pytest.raises(ValueError, match='Invalid input, only strings or integers are allowed'):
        roman_encode('invalid')

def test_roman_encode_out_of_range():
    with pytest.raises(ValueError, match='Input must be >= 1 and <= 3999'):
        roman_encode(0)
    with pytest.raises(ValueError, match='Input must be >= 1 and <= 3999'):
        roman_encode(4000)
