# file: thonny/roughparse.py:954-965
# asked: {"lines": [954, 962, 963, 965], "branches": []}
# gained: {"lines": [954, 962, 963, 965], "branches": []}

import pytest
from thonny.roughparse import _build_char_in_string_func

def test_build_char_in_string_func(monkeypatch):
    def mock_is_char_in_string(text_index):
        assert text_index == "1.0+5c"
        return True

    monkeypatch.setattr('thonny.roughparse._is_char_in_string', mock_is_char_in_string)
    
    func = _build_char_in_string_func("1.0")
    result = func(5)
    
    assert result == True
