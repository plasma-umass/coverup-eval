# file: string_utils/manipulation.py:611-634
# asked: {"lines": [611, 634], "branches": []}
# gained: {"lines": [611, 634], "branches": []}

import pytest
from string_utils.manipulation import roman_encode

def test_roman_encode_integer():
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(2020) == 'MMXX'
    assert roman_encode(3999) == 'MMMCMXCIX'

def test_roman_encode_string():
    assert roman_encode('37') == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'
    assert roman_encode('3999') == 'MMMCMXCIX'

def test_roman_encode_invalid_input():
    with pytest.raises(ValueError):
        roman_encode(0)
    with pytest.raises(ValueError):
        roman_encode(4000)
    with pytest.raises(ValueError):
        roman_encode('0')
    with pytest.raises(ValueError):
        roman_encode('4000')
    with pytest.raises(ValueError):
        roman_encode('invalid')

def test_roman_encode_edge_cases():
    assert roman_encode(1) == 'I'
    assert roman_encode(3999) == 'MMMCMXCIX'
    assert roman_encode('1') == 'I'
    assert roman_encode('3999') == 'MMMCMXCIX'
