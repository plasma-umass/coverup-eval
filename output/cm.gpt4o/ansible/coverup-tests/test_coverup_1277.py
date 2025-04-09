# file lib/ansible/utils/unsafe_proxy.py:109-114
# lines [113, 114]
# branches []

import pytest
from ansible.utils.unsafe_proxy import _wrap_sequence

def wrap_var(item):
    # Mock implementation of wrap_var for testing purposes
    return f"wrapped_{item}"

def test_wrap_sequence(mocker):
    # Mock the wrap_var function
    mocker.patch('ansible.utils.unsafe_proxy.wrap_var', side_effect=wrap_var)

    # Test with a list
    input_list = [1, 2, 3]
    expected_list = ['wrapped_1', 'wrapped_2', 'wrapped_3']
    result_list = _wrap_sequence(input_list)
    assert result_list == expected_list

    # Test with a tuple
    input_tuple = (4, 5, 6)
    expected_tuple = ('wrapped_4', 'wrapped_5', 'wrapped_6')
    result_tuple = _wrap_sequence(input_tuple)
    assert result_tuple == expected_tuple
