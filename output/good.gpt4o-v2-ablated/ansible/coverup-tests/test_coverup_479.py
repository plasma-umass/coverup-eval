# file: lib/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

import pytest
from unittest.mock import patch

# Assuming wrap_var is a function defined in the same module
from ansible.utils.unsafe_proxy import _wrap_dict, wrap_var

@pytest.fixture
def mock_wrap_var(mocker):
    return mocker.patch('ansible.utils.unsafe_proxy.wrap_var', side_effect=lambda x: f"wrapped_{x}")

def test_wrap_dict_with_empty_dict(mock_wrap_var):
    result = _wrap_dict({})
    assert result == {}
    mock_wrap_var.assert_not_called()

def test_wrap_dict_with_non_empty_dict(mock_wrap_var):
    input_dict = {'key1': 'value1', 'key2': 'value2'}
    expected_output = {'wrapped_key1': 'wrapped_value1', 'wrapped_key2': 'wrapped_value2'}
    
    result = _wrap_dict(input_dict)
    assert result == expected_output
    assert mock_wrap_var.call_count == 4
    mock_wrap_var.assert_any_call('key1')
    mock_wrap_var.assert_any_call('value1')
    mock_wrap_var.assert_any_call('key2')
    mock_wrap_var.assert_any_call('value2')
