# file: lib/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [109, 113, 114], "branches": []}
# gained: {"lines": [109, 113, 114], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_sequence, wrap_var

def test_wrap_sequence_with_list(mocker):
    mock_wrap_var = mocker.patch('ansible.utils.unsafe_proxy.wrap_var', side_effect=lambda x: f"wrapped_{x}")
    input_list = [1, 2, 3]
    result = _wrap_sequence(input_list)
    assert result == [f"wrapped_{i}" for i in input_list]
    mock_wrap_var.assert_has_calls([mocker.call(i) for i in input_list])

def test_wrap_sequence_with_tuple(mocker):
    mock_wrap_var = mocker.patch('ansible.utils.unsafe_proxy.wrap_var', side_effect=lambda x: f"wrapped_{x}")
    input_tuple = (1, 2, 3)
    result = _wrap_sequence(input_tuple)
    assert result == tuple(f"wrapped_{i}" for i in input_tuple)
    mock_wrap_var.assert_has_calls([mocker.call(i) for i in input_tuple])
