# file lib/ansible/utils/unsafe_proxy.py:105-106
# lines [105, 106]
# branches []

import pytest
from unittest.mock import patch

# Assuming wrap_var is a function in the same module
from ansible.utils.unsafe_proxy import _wrap_dict, wrap_var

def test_wrap_dict(mocker):
    # Mock the wrap_var function
    mock_wrap_var = mocker.patch('ansible.utils.unsafe_proxy.wrap_var', side_effect=lambda x: f"wrapped_{x}")

    # Test input
    test_input = {'key1': 'value1', 'key2': 'value2'}
    
    # Expected output
    expected_output = {'wrapped_key1': 'wrapped_value1', 'wrapped_key2': 'wrapped_value2'}
    
    # Call the function
    result = _wrap_dict(test_input)
    
    # Assertions
    assert result == expected_output
    mock_wrap_var.assert_any_call('key1')
    mock_wrap_var.assert_any_call('value1')
    mock_wrap_var.assert_any_call('key2')
    mock_wrap_var.assert_any_call('value2')
    assert mock_wrap_var.call_count == 4
