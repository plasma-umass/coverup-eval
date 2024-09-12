# file: string_utils/manipulation.py:116-156
# asked: {"lines": [116, 117, 118, 119, 122, 125, 128, 131, 133, 136, 142, 145, 146, 152, 154, 156], "branches": [[118, 119], [118, 122], [131, 133], [131, 156], [145, 146], [145, 152]]}
# gained: {"lines": [116, 117, 118, 119, 122, 125, 128, 131, 133, 136, 142, 145, 146, 152, 154, 156], "branches": [[118, 119], [118, 122], [131, 133], [131, 156], [145, 146], [145, 152]]}

import pytest
from string_utils.manipulation import __RomanNumbers
from string_utils.validation import is_full_string

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

def test_decode_case_insensitivity():
    assert __RomanNumbers.decode("iii") == 3
    assert __RomanNumbers.decode("Iv") == 4
    assert __RomanNumbers.decode("iX") == 9
    assert __RomanNumbers.decode("lViIi") == 58
    assert __RomanNumbers.decode("mCmXcIv") == 1994

def test_decode_complex_numerals():
    assert __RomanNumbers.decode("MMMDCCCLXXXVIII") == 3888
    assert __RomanNumbers.decode("MMMCMXCIX") == 3999

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: Ensure is_full_string behaves as expected
    monkeypatch.setattr("string_utils.validation.is_full_string", is_full_string)
    yield
    # Teardown: No specific teardown steps required
