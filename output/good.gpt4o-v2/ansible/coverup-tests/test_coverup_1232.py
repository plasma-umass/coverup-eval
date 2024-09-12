# file: lib/ansible/module_utils/compat/selinux.py:92-98
# asked: {"lines": [93, 94, 95, 96, 98], "branches": []}
# gained: {"lines": [93, 94, 95, 96, 98], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.compat.selinux import lgetfilecon_raw
from ctypes import c_char_p, byref

@pytest.fixture
def mock_selinux_lib():
    with patch('ansible.module_utils.compat.selinux._selinux_lib') as mock_lib:
        yield mock_lib

def test_lgetfilecon_raw_success(mock_selinux_lib):
    mock_selinux_lib.lgetfilecon_raw.return_value = 0
    mock_selinux_lib.freecon = MagicMock()
    path = '/some/path'
    
    result = lgetfilecon_raw(path)
    
    mock_selinux_lib.lgetfilecon_raw.assert_called_once()
    mock_selinux_lib.freecon.assert_called_once()
    assert result == [0, 'None']

def test_lgetfilecon_raw_failure(mock_selinux_lib):
    mock_selinux_lib.lgetfilecon_raw.return_value = -1
    mock_selinux_lib.freecon = MagicMock()
    path = '/some/path'
    
    result = lgetfilecon_raw(path)
    
    mock_selinux_lib.lgetfilecon_raw.assert_called_once()
    mock_selinux_lib.freecon.assert_called_once()
    assert result == [-1, 'None']
