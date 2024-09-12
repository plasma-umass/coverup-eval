# file: string_utils/manipulation.py:78-106
# asked: {"lines": [78, 79, 81, 83, 84, 86, 88, 89, 91, 92, 95, 97, 100, 104, 106], "branches": [[83, 84], [83, 86], [88, 89], [88, 91], [95, 97], [95, 106]]}
# gained: {"lines": [78, 79, 81, 83, 84, 86, 88, 89, 91, 92, 95, 97, 100, 104, 106], "branches": [[83, 84], [83, 86], [88, 89], [88, 91], [95, 97], [95, 106]]}

import pytest
from string_utils.manipulation import __RomanNumbers

def test_encode_valid_numbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(4) == 'IV'
    assert __RomanNumbers.encode(9) == 'IX'
    assert __RomanNumbers.encode(58) == 'LVIII'
    assert __RomanNumbers.encode(1994) == 'MCMXCIV'
    assert __RomanNumbers.encode(3999) == 'MMMCMXCIX'

def test_encode_invalid_input():
    with pytest.raises(ValueError, match='Invalid input, only strings or integers are allowed'):
        __RomanNumbers.encode('invalid')

def test_encode_out_of_range():
    with pytest.raises(ValueError, match='Input must be >= 1 and <= 3999'):
        __RomanNumbers.encode(0)
    with pytest.raises(ValueError, match='Input must be >= 1 and <= 3999'):
        __RomanNumbers.encode(4000)

def test_encode_string_input():
    assert __RomanNumbers.encode('1') == 'I'
    assert __RomanNumbers.encode('4') == 'IV'
    assert __RomanNumbers.encode('9') == 'IX'
    assert __RomanNumbers.encode('58') == 'LVIII'
    assert __RomanNumbers.encode('1994') == 'MCMXCIV'
    assert __RomanNumbers.encode('3999') == 'MMMCMXCIX'
