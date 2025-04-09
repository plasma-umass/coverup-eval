# file: lib/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [109, 113, 114], "branches": []}
# gained: {"lines": [109, 113, 114], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_sequence, wrap_var

def test_wrap_sequence_with_list():
    input_list = [1, 2, 3]
    result = _wrap_sequence(input_list)
    assert isinstance(result, list)
    assert result == input_list

def test_wrap_sequence_with_tuple():
    input_tuple = (1, 2, 3)
    result = _wrap_sequence(input_tuple)
    assert isinstance(result, tuple)
    assert result == input_tuple

def test_wrap_sequence_with_empty_list():
    input_list = []
    result = _wrap_sequence(input_list)
    assert isinstance(result, list)
    assert result == input_list

def test_wrap_sequence_with_empty_tuple():
    input_tuple = ()
    result = _wrap_sequence(input_tuple)
    assert isinstance(result, tuple)
    assert result == input_tuple

def test_wrap_sequence_with_nested_list():
    input_list = [1, [2, 3], 4]
    result = _wrap_sequence(input_list)
    assert isinstance(result, list)
    assert result[1] == [2, 3]

def test_wrap_sequence_with_nested_tuple():
    input_tuple = (1, (2, 3), 4)
    result = _wrap_sequence(input_tuple)
    assert isinstance(result, tuple)
    assert result[1] == (2, 3)
