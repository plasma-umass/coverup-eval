# file string_utils/manipulation.py:611-634
# lines [611, 634]
# branches []

import pytest
from string_utils.manipulation import roman_encode

def test_roman_encode():
    # Test with integer input
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(2020) == 'MMXX'
    
    # Test with string input
    assert roman_encode('37') == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'
    
    # Test with edge cases
    assert roman_encode(1) == 'I'
    assert roman_encode(3999) == 'MMMCMXCIX'
    
    # Test with invalid input
    with pytest.raises(ValueError):
        roman_encode(0)
    with pytest.raises(ValueError):
        roman_encode(4000)
    with pytest.raises(ValueError):
        roman_encode(-1)
    with pytest.raises(ValueError):
        roman_encode('invalid')
    with pytest.raises(ValueError):
        roman_encode('4000')
