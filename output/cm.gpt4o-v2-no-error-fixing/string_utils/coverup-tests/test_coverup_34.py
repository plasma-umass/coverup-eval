# file: string_utils/manipulation.py:116-156
# asked: {"lines": [116, 117, 118, 119, 122, 125, 128, 131, 133, 136, 142, 145, 146, 152, 154, 156], "branches": [[118, 119], [118, 122], [131, 133], [131, 156], [145, 146], [145, 152]]}
# gained: {"lines": [116, 117, 118, 119, 122, 125, 128, 131, 133, 136, 142, 145, 146, 152, 154, 156], "branches": [[118, 119], [118, 122], [131, 133], [131, 156], [145, 146], [145, 152]]}

import pytest
from string_utils.manipulation import __RomanNumbers
from string_utils.errors import InvalidInputError

def test_decode_valid_roman_numerals():
    assert __RomanNumbers.decode("III") == 3
    assert __RomanNumbers.decode("IV") == 4
    assert __RomanNumbers.decode("IX") == 9
    assert __RomanNumbers.decode("LVIII") == 58
    assert __RomanNumbers.decode("MCMXCIV") == 1994

def test_decode_invalid_input():
    with pytest.raises(ValueError, match="Input must be a non empty string"):
        __RomanNumbers.decode("")
    with pytest.raises(ValueError, match="Input must be a non empty string"):
        __RomanNumbers.decode(" ")
    with pytest.raises(ValueError, match="Input must be a non empty string"):
        __RomanNumbers.decode(None)

def test_decode_invalid_roman_numerals():
    with pytest.raises(ValueError, match="Invalid token found: \"A\""):
        __RomanNumbers.decode("A")
    with pytest.raises(ValueError, match="Invalid token found: \"B\""):
        __RomanNumbers.decode("ABCD")
    with pytest.raises(ValueError, match="Invalid token found: \"Z\""):
        __RomanNumbers.decode("XYZ")

@pytest.fixture
def mock_reverse(monkeypatch):
    def mock_reverse(input_string):
        return input_string[::-1]
    monkeypatch.setattr("string_utils.manipulation.reverse", mock_reverse)

def test_decode_with_mock_reverse(mock_reverse):
    assert __RomanNumbers.decode("III") == 3
    assert __RomanNumbers.decode("IV") == 4
    assert __RomanNumbers.decode("IX") == 9
    assert __RomanNumbers.decode("LVIII") == 58
    assert __RomanNumbers.decode("MCMXCIV") == 1994
