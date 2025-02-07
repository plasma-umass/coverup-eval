# file: lib/ansible/module_utils/compat/selinux.py:77-80
# asked: {"lines": [78, 79, 80], "branches": []}
# gained: {"lines": [78, 79, 80], "branches": []}

import pytest
from unittest import mock
from ctypes import c_int, byref

# Mocking _selinux_lib.selinux_getenforcemode
@pytest.fixture
def mock_selinux_lib(monkeypatch):
    mock_lib = mock.Mock()
    monkeypatch.setattr('ansible.module_utils.compat.selinux._selinux_lib', mock_lib)
    return mock_lib

def test_selinux_getenforcemode_success(mock_selinux_lib):
    from ansible.module_utils.compat.selinux import selinux_getenforcemode

    # Mock the return value of selinux_getenforcemode
    mock_selinux_lib.selinux_getenforcemode.return_value = 0
    enforcemode_value = 1

    def side_effect(arg):
        arg._obj.value = enforcemode_value
        return 0

    mock_selinux_lib.selinux_getenforcemode.side_effect = side_effect

    result = selinux_getenforcemode()

    assert result == [0, enforcemode_value]
    mock_selinux_lib.selinux_getenforcemode.assert_called_once()

def test_selinux_getenforcemode_failure(mock_selinux_lib):
    from ansible.module_utils.compat.selinux import selinux_getenforcemode

    # Mock the return value of selinux_getenforcemode
    mock_selinux_lib.selinux_getenforcemode.return_value = -1
    enforcemode_value = 0

    def side_effect(arg):
        arg._obj.value = enforcemode_value
        return -1

    mock_selinux_lib.selinux_getenforcemode.side_effect = side_effect

    result = selinux_getenforcemode()

    assert result == [-1, enforcemode_value]
    mock_selinux_lib.selinux_getenforcemode.assert_called_once()
