# file: lib/ansible/module_utils/compat/selinux.py:77-80
# asked: {"lines": [78, 79, 80], "branches": []}
# gained: {"lines": [78, 79, 80], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ctypes import c_int, byref

# Assuming the function is imported from the module
# from ansible.module_utils.compat.selinux import selinux_getenforcemode

def test_selinux_getenforcemode_success(monkeypatch):
    mock_selinux_lib = MagicMock()
    mock_selinux_lib.selinux_getenforcemode.return_value = 0
    monkeypatch.setattr('ansible.module_utils.compat.selinux._selinux_lib', mock_selinux_lib)

    from ansible.module_utils.compat.selinux import selinux_getenforcemode

    result = selinux_getenforcemode()
    assert result == [0, 0]
    mock_selinux_lib.selinux_getenforcemode.assert_called_once()

def test_selinux_getenforcemode_failure(monkeypatch):
    mock_selinux_lib = MagicMock()
    mock_selinux_lib.selinux_getenforcemode.return_value = -1
    monkeypatch.setattr('ansible.module_utils.compat.selinux._selinux_lib', mock_selinux_lib)

    from ansible.module_utils.compat.selinux import selinux_getenforcemode

    result = selinux_getenforcemode()
    assert result == [-1, 0]
    mock_selinux_lib.selinux_getenforcemode.assert_called_once()
