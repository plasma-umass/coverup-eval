# file: lib/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [109, 113, 114], "branches": []}
# gained: {"lines": [109, 113, 114], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_sequence, wrap_var

def test_wrap_sequence_with_list(monkeypatch):
    def mock_wrap_var(item):
        return f"wrapped_{item}"
    
    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)
    
    input_list = [1, 2, 3]
    expected_output = ["wrapped_1", "wrapped_2", "wrapped_3"]
    
    result = _wrap_sequence(input_list)
    
    assert result == expected_output

def test_wrap_sequence_with_tuple(monkeypatch):
    def mock_wrap_var(item):
        return f"wrapped_{item}"
    
    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)
    
    input_tuple = (1, 2, 3)
    expected_output = ("wrapped_1", "wrapped_2", "wrapped_3")
    
    result = _wrap_sequence(input_tuple)
    
    assert result == expected_output
