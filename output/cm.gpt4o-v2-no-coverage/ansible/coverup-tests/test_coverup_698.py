# file: lib/ansible/module_utils/compat/selinux.py:101-107
# asked: {"lines": [101, 102, 103, 104, 105, 107], "branches": []}
# gained: {"lines": [101, 102, 103, 104, 105, 107], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.compat.selinux import matchpathcon
from ctypes import c_char_p, byref

@pytest.fixture
def mock_selinux_lib():
    with patch('ansible.module_utils.compat.selinux._selinux_lib') as mock_lib:
        yield mock_lib

def test_matchpathcon_success(mock_selinux_lib):
    mock_con = c_char_p(b'system_u:object_r:var_t:s0')
    mock_selinux_lib.matchpathcon.return_value = 0
    mock_selinux_lib.freecon.return_value = None

    with patch('ansible.module_utils.compat.selinux.c_char_p', return_value=mock_con):
        result = matchpathcon('/var/www', 0o755)
    
    assert result == [0, 'system_u:object_r:var_t:s0']
    assert mock_selinux_lib.matchpathcon.call_count == 1
    assert mock_selinux_lib.freecon.call_count == 1

def test_matchpathcon_failure(mock_selinux_lib):
    mock_con = c_char_p(b'')
    mock_selinux_lib.matchpathcon.return_value = -1
    mock_selinux_lib.freecon.return_value = None

    with patch('ansible.module_utils.compat.selinux.c_char_p', return_value=mock_con):
        result = matchpathcon('/invalid/path', 0o755)
    
    assert result == [-1, '']
    assert mock_selinux_lib.matchpathcon.call_count == 1
    assert mock_selinux_lib.freecon.call_count == 1
