# file string_utils/manipulation.py:36-51
# lines [36, 38, 40, 42, 44, 46, 50]
# branches []

import pytest
from string_utils.manipulation import __RomanNumbers

def test_roman_numbers_mappings():
    # Access the private class and its attributes to ensure they are correctly set
    roman_numbers = __RomanNumbers()
    
    expected_mappings = [
        {1: 'I', 5: 'V'},
        {1: 'X', 5: 'L'},
        {1: 'C', 5: 'D'},
        {1: 'M'},
    ]
    
    expected_reversed_mappings = [
        {'I': 1, 'V': 5},
        {'X': 1, 'L': 5},
        {'C': 1, 'D': 5},
        {'M': 1},
    ]
    
    assert roman_numbers._RomanNumbers__mappings == expected_mappings
    assert roman_numbers._RomanNumbers__reversed_mappings == expected_reversed_mappings

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # No specific cleanup required for this test
