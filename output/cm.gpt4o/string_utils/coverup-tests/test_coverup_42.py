# file string_utils/manipulation.py:108-114
# lines [108, 109, 110, 111, 112, 114]
# branches ['110->111', '110->114', '111->110', '111->112']

import pytest
from string_utils.manipulation import __RomanNumbers

def test___index_for_sign_valid():
    # Assuming __reversed_mappings is a class attribute of __RomanNumbers
    __RomanNumbers._RomanNumbers__reversed_mappings = [{'I': 1}, {'V': 5}, {'X': 10}]
    assert __RomanNumbers._RomanNumbers__index_for_sign('I') == 0
    assert __RomanNumbers._RomanNumbers__index_for_sign('V') == 1
    assert __RomanNumbers._RomanNumbers__index_for_sign('X') == 2

def test___index_for_sign_invalid():
    __RomanNumbers._RomanNumbers__reversed_mappings = [{'I': 1}, {'V': 5}, {'X': 10}]
    with pytest.raises(ValueError, match='Invalid token found: "A"'):
        __RomanNumbers._RomanNumbers__index_for_sign('A')

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Clean up any modifications to __RomanNumbers
    if hasattr(__RomanNumbers, '_RomanNumbers__reversed_mappings'):
        del __RomanNumbers._RomanNumbers__reversed_mappings
