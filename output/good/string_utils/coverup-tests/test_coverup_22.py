# file string_utils/manipulation.py:78-106
# lines [78, 79, 81, 83, 84, 86, 88, 89, 91, 92, 95, 97, 100, 104, 106]
# branches ['83->84', '83->86', '88->89', '88->91', '95->97', '95->106']

import pytest
from string_utils.manipulation import __RomanNumbers

def test_encode_invalid_input_type():
    with pytest.raises(ValueError) as excinfo:
        __RomanNumbers.encode(3.14)  # float is not allowed
    assert "Invalid input, only strings or integers are allowed" in str(excinfo.value)

def test_encode_invalid_input_value():
    with pytest.raises(ValueError) as excinfo:
        __RomanNumbers.encode("4000")  # value out of range
    assert "Input must be >= 1 and <= 3999" in str(excinfo.value)

def test_encode_valid_input(mocker):
    mocker.patch.object(__RomanNumbers, '_RomanNumbers__encode_digit', side_effect=lambda index, digit: 'I' * digit)
    result = __RomanNumbers.encode(3)
    assert result == 'III'
