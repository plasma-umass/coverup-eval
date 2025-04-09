# file lib/ansible/utils/unsafe_proxy.py:141-142
# lines [142]
# branches []

import pytest
from ansible.utils.unsafe_proxy import to_unsafe_bytes, wrap_var, to_bytes

def test_to_unsafe_bytes(mocker):
    # Mock the to_bytes function to ensure it gets called with the correct arguments
    mock_to_bytes = mocker.patch('ansible.utils.unsafe_proxy.to_bytes', return_value=b'test_bytes')
    # Mock the wrap_var function to ensure it gets called with the correct arguments
    mock_wrap_var = mocker.patch('ansible.utils.unsafe_proxy.wrap_var', return_value='wrapped_test_bytes')

    # Call the function with test arguments
    result = to_unsafe_bytes('test_string', encoding='utf-8')

    # Assert that to_bytes was called with the correct arguments
    mock_to_bytes.assert_called_once_with('test_string', encoding='utf-8')
    # Assert that wrap_var was called with the result of to_bytes
    mock_wrap_var.assert_called_once_with(b'test_bytes')
    # Assert that the result of to_unsafe_bytes is the result of wrap_var
    assert result == 'wrapped_test_bytes'
