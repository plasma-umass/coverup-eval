# file: string_utils/manipulation.py:78-106
# asked: {"lines": [78, 79, 81, 83, 84, 86, 88, 89, 91, 92, 95, 97, 100, 104, 106], "branches": [[83, 84], [83, 86], [88, 89], [88, 91], [95, 97], [95, 106]]}
# gained: {"lines": [78, 79, 81, 83, 84, 86, 88, 89, 91, 92, 95, 97, 100, 104, 106], "branches": [[83, 84], [83, 86], [88, 89], [88, 91], [95, 97], [95, 106]]}

import pytest
from string_utils.manipulation import __RomanNumbers

def test_encode_valid_integer():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(3999) == 'MMMCMXCIX'

def test_encode_valid_string():
    assert __RomanNumbers.encode('1') == 'I'
    assert __RomanNumbers.encode('3999') == 'MMMCMXCIX'

def test_encode_invalid_string():
    with pytest.raises(ValueError, match='Invalid input, only strings or integers are allowed'):
        __RomanNumbers.encode('invalid')

def test_encode_out_of_range_low():
    with pytest.raises(ValueError, match='Input must be >= 1 and <= 3999'):
        __RomanNumbers.encode(0)

def test_encode_out_of_range_high():
    with pytest.raises(ValueError, match='Input must be >= 1 and <= 3999'):
        __RomanNumbers.encode(4000)

def test_encode_negative_integer():
    with pytest.raises(ValueError, match='Input must be >= 1 and <= 3999'):
        __RomanNumbers.encode(-1)

def test_encode_empty_string():
    with pytest.raises(ValueError, match='Invalid input, only strings or integers are allowed'):
        __RomanNumbers.encode('')

def test_encode_non_integer_string():
    with pytest.raises(ValueError, match='Invalid input, only strings or integers are allowed'):
        __RomanNumbers.encode('3.14')
