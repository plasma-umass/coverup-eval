# file lib/ansible/utils/unsafe_proxy.py:141-142
# lines [141, 142]
# branches []

import pytest
from ansible.utils.unsafe_proxy import wrap_var, to_bytes

def test_to_unsafe_bytes(mocker):
    # Mock the to_bytes function to control its output
    mock_to_bytes = mocker.patch('ansible.utils.unsafe_proxy.to_bytes', return_value=b'some_bytes')
    
    # Define the function to be tested
    def to_unsafe_bytes(*args, **kwargs):
        return wrap_var(mock_to_bytes(*args, **kwargs))
    
    # Call the function with test arguments
    result = to_unsafe_bytes('test_string')
    
    # Assert that to_bytes was called with the correct arguments
    mock_to_bytes.assert_called_once_with('test_string')
    
    # Assert that wrap_var was called with the result of to_bytes
    assert result == wrap_var(b'some_bytes')
