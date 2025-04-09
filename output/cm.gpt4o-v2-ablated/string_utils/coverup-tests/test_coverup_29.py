# file: string_utils/manipulation.py:637-649
# asked: {"lines": [637, 649], "branches": []}
# gained: {"lines": [637, 649], "branches": []}

import pytest
from string_utils.manipulation import roman_decode

class MockRomanNumbers:
    @staticmethod
    def decode(input_string):
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        prev_value = 0
        for char in reversed(input_string):
            value = roman_to_int[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

@pytest.fixture
def mock_roman_numbers(monkeypatch):
    monkeypatch.setattr('string_utils.manipulation.__RomanNumbers', MockRomanNumbers)

def test_roman_decode_valid(mock_roman_numbers):
    assert roman_decode('VII') == 7
    assert roman_decode('IV') == 4
    assert roman_decode('IX') == 9
    assert roman_decode('LVIII') == 58
    assert roman_decode('MCMXCIV') == 1994

def test_roman_decode_empty_string(mock_roman_numbers):
    assert roman_decode('') == 0

def test_roman_decode_single_character(mock_roman_numbers):
    assert roman_decode('I') == 1
    assert roman_decode('V') == 5
    assert roman_decode('X') == 10
    assert roman_decode('L') == 50
    assert roman_decode('C') == 100
    assert roman_decode('D') == 500
    assert roman_decode('M') == 1000
