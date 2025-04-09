# file: string_utils/manipulation.py:637-649
# asked: {"lines": [637, 649], "branches": []}
# gained: {"lines": [637, 649], "branches": []}

import pytest
from string_utils.manipulation import roman_decode

def test_roman_decode_valid():
    assert roman_decode('VII') == 7
    assert roman_decode('IV') == 4
    assert roman_decode('XII') == 12

def test_roman_decode_invalid(monkeypatch):
    class MockRomanNumbers:
        @staticmethod
        def decode(input_string):
            raise ValueError("Invalid Roman numeral")

    monkeypatch.setattr('string_utils.manipulation.__RomanNumbers', MockRomanNumbers)
    
    with pytest.raises(ValueError, match="Invalid Roman numeral"):
        roman_decode('IIII')

def test_roman_decode_empty_string(monkeypatch):
    class MockRomanNumbers:
        @staticmethod
        def decode(input_string):
            if input_string == "":
                return 0
            raise ValueError("Invalid Roman numeral")

    monkeypatch.setattr('string_utils.manipulation.__RomanNumbers', MockRomanNumbers)
    
    assert roman_decode('') == 0
