# file string_utils/manipulation.py:116-156
# lines [116, 117, 118, 119, 122, 125, 128, 131, 133, 136, 142, 145, 146, 152, 154, 156]
# branches ['118->119', '118->122', '131->133', '131->156', '145->146', '145->152']

import pytest
from string_utils.manipulation import __RomanNumbers

def test_decode_valid_roman_numerals(mocker):
    mock_dependencies(mocker)
    assert __RomanNumbers.decode("III") == 3
    assert __RomanNumbers.decode("IV") == 4
    assert __RomanNumbers.decode("IX") == 9
    assert __RomanNumbers.decode("LVIII") == 58
    assert __RomanNumbers.decode("MCMXCIV") == 1994

def test_decode_invalid_roman_numerals(mocker):
    mocker.patch('string_utils.manipulation.is_full_string', return_value=False)
    with pytest.raises(ValueError, match='Input must be a non empty string'):
        __RomanNumbers.decode("")
    with pytest.raises(ValueError, match='Input must be a non empty string'):
        __RomanNumbers.decode(" ")

def test_decode_non_roman_characters(mocker):
    mock_dependencies(mocker)
    with pytest.raises(KeyError):
        __RomanNumbers.decode("ABCD")

def test_decode_mixed_case_roman_numerals(mocker):
    mock_dependencies(mocker)
    assert __RomanNumbers.decode("mCmXcIv") == 1994

def mock_dependencies(mocker):
    mocker.patch('string_utils.manipulation.is_full_string', return_value=True)
    mocker.patch('string_utils.manipulation.reverse', side_effect=lambda s: s[::-1])
    mocker.patch.object(__RomanNumbers, '_RomanNumbers__index_for_sign', side_effect=lambda s: {'I': 0, 'V': 0, 'X': 1, 'L': 1, 'C': 2, 'D': 2, 'M': 3}[s])
    mocker.patch.object(__RomanNumbers, '_RomanNumbers__reversed_mappings', [{ 'I': 1, 'V': 5 }, { 'X': 1, 'L': 5 }, { 'C': 1, 'D': 5 }, { 'M': 1 }])
