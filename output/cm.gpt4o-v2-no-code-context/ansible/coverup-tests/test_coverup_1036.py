# file: lib/ansible/module_utils/compat/selinux.py:83-89
# asked: {"lines": [84, 85, 86, 87, 89], "branches": []}
# gained: {"lines": [84, 85, 86, 87, 89], "branches": []}

import pytest
from ctypes import c_char_p, byref
from unittest.mock import Mock, patch

# Assuming the function selinux_getpolicytype is imported from the module
from ansible.module_utils.compat.selinux import selinux_getpolicytype

@pytest.fixture
def mock_selinux_lib(mocker):
    selinux_lib = mocker.patch('ansible.module_utils.compat.selinux._selinux_lib')
    return selinux_lib

def test_selinux_getpolicytype_success(mock_selinux_lib):
    mock_selinux_lib.selinux_getpolicytype.return_value = 0
    mock_con = c_char_p(b"test_policy")
    mock_selinux_lib.freecon = Mock()
    
    with patch('ansible.module_utils.compat.selinux.c_char_p', return_value=mock_con):
        result = selinux_getpolicytype()
    
    assert result == [0, "test_policy"]
    assert mock_selinux_lib.selinux_getpolicytype.call_count == 1
    assert mock_selinux_lib.selinux_getpolicytype.call_args[0][0]._obj.value == mock_con.value
    mock_selinux_lib.freecon.assert_called_once_with(mock_con)

def test_selinux_getpolicytype_failure(mock_selinux_lib):
    mock_selinux_lib.selinux_getpolicytype.return_value = -1
    mock_con = c_char_p(b"")
    mock_selinux_lib.freecon = Mock()
    
    with patch('ansible.module_utils.compat.selinux.c_char_p', return_value=mock_con):
        result = selinux_getpolicytype()
    
    assert result == [-1, ""]
    assert mock_selinux_lib.selinux_getpolicytype.call_count == 1
    assert mock_selinux_lib.selinux_getpolicytype.call_args[0][0]._obj.value == mock_con.value
    mock_selinux_lib.freecon.assert_called_once_with(mock_con)
