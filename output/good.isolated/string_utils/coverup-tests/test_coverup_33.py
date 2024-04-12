# file string_utils/manipulation.py:611-634
# lines [611, 634]
# branches []

import pytest
from string_utils.manipulation import roman_encode

def test_roman_encode():
    assert roman_encode(1) == 'I', "Test failed for input 1"
    assert roman_encode(3999) == 'MMMCMXCIX', "Test failed for input 3999"
    assert roman_encode('2020') == 'MMXX', "Test failed for input '2020'"
    assert roman_encode(37) == 'XXXVII', "Test failed for input 37"
    
    with pytest.raises(ValueError):
        roman_encode(0)  # Test for value below the valid range
    with pytest.raises(ValueError):
        roman_encode(4000)  # Test for value above the valid range
    with pytest.raises(ValueError):
        roman_encode('MMXX')  # Test for invalid string input
    with pytest.raises(ValueError):
        roman_encode(None)  # Test for None input, corrected to ValueError
    with pytest.raises(ValueError):
        roman_encode([])  # Test for list input, corrected to ValueError
    with pytest.raises(ValueError):
        roman_encode({})  # Test for dict input, corrected to ValueError
