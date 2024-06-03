# file string_utils/manipulation.py:637-649
# lines [649]
# branches []

import pytest
from string_utils.manipulation import roman_decode

class MockRomanNumbers:
    @staticmethod
    def decode(input_string):
        if input_string == "VII":
            return 7
        raise ValueError("Invalid Roman numeral")

@pytest.fixture
def mock_roman_numbers(mocker):
    mocker.patch('string_utils.manipulation.__RomanNumbers', MockRomanNumbers)

def test_roman_decode_valid(mock_roman_numbers):
    assert roman_decode("VII") == 7

def test_roman_decode_invalid(mock_roman_numbers):
    with pytest.raises(ValueError, match="Invalid Roman numeral"):
        roman_decode("INVALID")
