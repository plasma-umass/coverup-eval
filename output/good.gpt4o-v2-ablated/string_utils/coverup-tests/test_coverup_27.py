# file: string_utils/manipulation.py:611-634
# asked: {"lines": [611, 634], "branches": []}
# gained: {"lines": [611, 634], "branches": []}

import pytest
from string_utils.manipulation import roman_encode

class MockRomanNumbers:
    @staticmethod
    def encode(input_number):
        if input_number == 37:
            return 'XXXVII'
        elif input_number == '2020':
            return 'MMXX'
        elif input_number == 1:
            return 'I'
        elif input_number == 3999:
            return 'MMMCMXCIX'
        else:
            raise ValueError("Input out of range")

@pytest.fixture
def mock_roman_numbers(monkeypatch):
    monkeypatch.setattr('string_utils.manipulation.__RomanNumbers', MockRomanNumbers)

def test_roman_encode_37(mock_roman_numbers):
    result = roman_encode(37)
    assert result == 'XXXVII'

def test_roman_encode_2020(mock_roman_numbers):
    result = roman_encode('2020')
    assert result == 'MMXX'

def test_roman_encode_1(mock_roman_numbers):
    result = roman_encode(1)
    assert result == 'I'

def test_roman_encode_3999(mock_roman_numbers):
    result = roman_encode(3999)
    assert result == 'MMMCMXCIX'

def test_roman_encode_invalid(mock_roman_numbers):
    with pytest.raises(ValueError, match="Input out of range"):
        roman_encode(4000)
