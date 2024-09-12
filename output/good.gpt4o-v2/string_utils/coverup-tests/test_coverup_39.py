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
    def mock_is_full_string(input_string):
        return False

    monkeypatch.setattr('string_utils.validation.is_full_string', mock_is_full_string)
    
    with pytest.raises(ValueError, match='Input must be a non empty string'):
        roman_decode('')

def test_roman_decode_case_insensitive():
    assert roman_decode('vii') == 7
    assert roman_decode('iV') == 4
    assert roman_decode('xii') == 12
