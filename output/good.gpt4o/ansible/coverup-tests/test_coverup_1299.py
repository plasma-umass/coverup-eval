# file lib/ansible/module_utils/common/validation.py:530-535
# lines [534, 535]
# branches []

import os
import pytest
from unittest.mock import patch
from ansible.module_utils.common.validation import check_type_path

def test_check_type_path(mocker):
    # Mock check_type_str to return a specific value
    mock_check_type_str = mocker.patch('ansible.module_utils.common.validation.check_type_str', return_value='~testuser/testpath')
    
    # Mock os.path.expandvars to return a specific value
    mock_expandvars = mocker.patch('os.path.expandvars', return_value='~testuser/testpath')
    # Mock os.path.expanduser to return a specific value
    mock_expanduser = mocker.patch('os.path.expanduser', return_value='/home/testuser/testpath')
    
    # Call the function with a dummy value
    result = check_type_path('dummy_value')
    
    # Assertions to verify the function behavior
    mock_check_type_str.assert_called_once_with('dummy_value')
    mock_expandvars.assert_called_once_with('~testuser/testpath')
    mock_expanduser.assert_called_once_with('~testuser/testpath')
    assert result == '/home/testuser/testpath'
