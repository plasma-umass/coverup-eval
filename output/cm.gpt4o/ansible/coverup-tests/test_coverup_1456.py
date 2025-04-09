# file lib/ansible/module_utils/compat/selinux.py:77-80
# lines [78, 79, 80]
# branches []

import pytest
from unittest import mock
from ctypes import c_int, byref

# Assuming the function is imported from the module
from ansible.module_utils.compat.selinux import selinux_getenforcemode

@pytest.fixture
def mock_selinux_lib(mocker):
    mock_lib = mocker.patch('ansible.module_utils.compat.selinux._selinux_lib')
    return mock_lib

def test_selinux_getenforcemode(mock_selinux_lib):
    # Mock the selinux_getenforcemode function
    mock_selinux_lib.selinux_getenforcemode.return_value = 0
    mock_enforcemode = c_int(1)
    
    def side_effect(arg):
        arg._obj.value = mock_enforcemode.value
        return 0

    mock_selinux_lib.selinux_getenforcemode.side_effect = side_effect

    result = selinux_getenforcemode()

    # Assertions to verify the postconditions
    assert result == [0, 1]
    mock_selinux_lib.selinux_getenforcemode.assert_called_once()
