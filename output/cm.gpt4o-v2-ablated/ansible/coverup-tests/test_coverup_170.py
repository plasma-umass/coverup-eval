# file: lib/ansible/module_utils/facts/system/service_mgr.py:55-63
# asked: {"lines": [55, 56, 58, 61, 62, 63], "branches": [[58, 61], [58, 63], [61, 62], [61, 63]]}
# gained: {"lines": [55, 56, 58, 61, 62, 63], "branches": [[58, 61], [58, 63], [61, 62], [61, 63]]}

import os
import pytest
from unittest.mock import MagicMock, patch

from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module():
    return MagicMock()

def test_is_systemd_managed_offline_systemctl_exists_and_is_symlink(mock_module, monkeypatch):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    monkeypatch.setattr(os.path, 'islink', lambda x: x == '/sbin/init')
    monkeypatch.setattr(os.path, 'basename', lambda x: 'systemd')
    monkeypatch.setattr(os, 'readlink', lambda x: '/lib/systemd/systemd')

    result = ServiceMgrFactCollector.is_systemd_managed_offline(mock_module)
    assert result is True

def test_is_systemd_managed_offline_systemctl_exists_and_not_symlink(mock_module, monkeypatch):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    monkeypatch.setattr(os.path, 'islink', lambda x: x == '/sbin/init')
    monkeypatch.setattr(os.path, 'basename', lambda x: 'not_systemd')
    monkeypatch.setattr(os, 'readlink', lambda x: '/lib/not_systemd')

    result = ServiceMgrFactCollector.is_systemd_managed_offline(mock_module)
    assert result is False

def test_is_systemd_managed_offline_systemctl_not_exists(mock_module):
    mock_module.get_bin_path.return_value = None

    result = ServiceMgrFactCollector.is_systemd_managed_offline(mock_module)
    assert result is False

def test_is_systemd_managed_offline_init_not_symlink(mock_module, monkeypatch):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    monkeypatch.setattr(os.path, 'islink', lambda x: False)

    result = ServiceMgrFactCollector.is_systemd_managed_offline(mock_module)
    assert result is False
