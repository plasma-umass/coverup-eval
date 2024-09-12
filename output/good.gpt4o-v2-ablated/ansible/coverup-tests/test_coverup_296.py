# file: lib/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [109, 113, 114], "branches": []}
# gained: {"lines": [109, 113, 114], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_sequence

def wrap_var(item):
    # Mock implementation of wrap_var for testing purposes
    return f"wrapped_{item}"

def test_wrap_sequence_with_list():
    input_list = [1, 2, 3]
    expected_output = ["wrapped_1", "wrapped_2", "wrapped_3"]
    result = _wrap_sequence(input_list)
    assert result == expected_output

def test_wrap_sequence_with_tuple():
    input_tuple = (1, 2, 3)
    expected_output = ("wrapped_1", "wrapped_2", "wrapped_3")
    result = _wrap_sequence(input_tuple)
    assert result == expected_output

def test_wrap_sequence_with_empty_list():
    input_list = []
    expected_output = []
    result = _wrap_sequence(input_list)
    assert result == expected_output

def test_wrap_sequence_with_empty_tuple():
    input_tuple = ()
    expected_output = ()
    result = _wrap_sequence(input_tuple)
    assert result == expected_output

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Ensure wrap_var is patched correctly for each test
    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', wrap_var)
