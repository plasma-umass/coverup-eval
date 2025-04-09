# file: string_utils/manipulation.py:108-114
# asked: {"lines": [108, 109, 110, 111, 112, 114], "branches": [[110, 111], [110, 114], [111, 110], [111, 112]]}
# gained: {"lines": [108, 109, 110, 111, 112, 114], "branches": [[110, 111], [110, 114], [111, 110], [111, 112]]}

import pytest
from string_utils.manipulation import __RomanNumbers

def test_index_for_sign_valid(monkeypatch):
    # Mock the __reversed_mappings attribute
    mock_mappings = [{'I': 1}, {'V': 5}, {'X': 10}]
    monkeypatch.setattr(__RomanNumbers, '_RomanNumbers__reversed_mappings', mock_mappings)
    
    assert __RomanNumbers._RomanNumbers__index_for_sign('I') == 0
    assert __RomanNumbers._RomanNumbers__index_for_sign('V') == 1
    assert __RomanNumbers._RomanNumbers__index_for_sign('X') == 2

def test_index_for_sign_invalid(monkeypatch):
    # Mock the __reversed_mappings attribute
    mock_mappings = [{'I': 1}, {'V': 5}, {'X': 10}]
    monkeypatch.setattr(__RomanNumbers, '_RomanNumbers__reversed_mappings', mock_mappings)
    
    with pytest.raises(ValueError, match='Invalid token found: "A"'):
        __RomanNumbers._RomanNumbers__index_for_sign('A')
