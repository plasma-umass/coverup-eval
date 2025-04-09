# file lib/ansible/module_utils/common/validation.py:530-535
# lines [530, 534, 535]
# branches []

import os
import pytest
from ansible.module_utils.common.validation import check_type_path

# Test function to cover check_type_path
def test_check_type_path_expansion(mocker):
    # Mock the os.path.expanduser and os.path.expandvars to control their behavior
    mock_expanduser = mocker.patch('os.path.expanduser', return_value='expanded_user_path')
    mock_expandvars = mocker.patch('os.path.expandvars', return_value='expanded_var_path')

    # Test with a string that contains a user tilde and an environment variable
    input_value = '~/some/path:$VARIABLE'
    expected_result = 'expanded_user_path'

    # Call the function with the test input
    result = check_type_path(input_value)

    # Verify that the os.path.expandvars was called with the original input
    mock_expandvars.assert_called_once_with(input_value)
    # Verify that the os.path.expanduser was called with the result of expandvars
    mock_expanduser.assert_called_once_with('expanded_var_path')
    # Verify the result is as expected
    assert result == expected_result
