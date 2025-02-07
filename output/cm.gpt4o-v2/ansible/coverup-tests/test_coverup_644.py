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
    mock_selinux_lib.matchpathcon = MagicMock(return_value=0)
    mock_selinux_lib.freecon = MagicMock()
    path = "/some/path"
    mode = 0o755

    result = matchpathcon(path, mode)

    mock_selinux_lib.matchpathcon.assert_called_once()
    mock_selinux_lib.freecon.assert_called_once()
    assert result == [0, 'None']

def test_matchpathcon_failure(mock_selinux_lib):
    mock_selinux_lib.matchpathcon = MagicMock(return_value=-1)
    mock_selinux_lib.freecon = MagicMock()
    path = "/some/path"
    mode = 0o755

    result = matchpathcon(path, mode)

    mock_selinux_lib.matchpathcon.assert_called_once()
    mock_selinux_lib.freecon.assert_called_once()
    assert result == [-1, 'None']
