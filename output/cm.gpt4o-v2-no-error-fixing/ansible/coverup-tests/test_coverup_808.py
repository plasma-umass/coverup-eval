# file: lib/ansible/module_utils/compat/selinux.py:77-80
# asked: {"lines": [78, 79, 80], "branches": []}
# gained: {"lines": [78, 79, 80], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ctypes import c_int

# Assuming the selinux_getenforcemode function is imported from the module
from ansible.module_utils.compat.selinux import selinux_getenforcemode

@patch('ansible.module_utils.compat.selinux._selinux_lib.selinux_getenforcemode')
def test_selinux_getenforcemode(mock_selinux_getenforcemode):
    # Mock the return value of the selinux_getenforcemode function
    mock_selinux_getenforcemode.return_value = 0
    mock_enforcemode = c_int(1)
    
    with patch('ansible.module_utils.compat.selinux.c_int', return_value=mock_enforcemode):
        result = selinux_getenforcemode()
    
    # Assert that the selinux_getenforcemode function was called once
    mock_selinux_getenforcemode.assert_called_once()
    
    # Assert the return value
    assert result == [0, 1]
