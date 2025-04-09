# file: lib/ansible/module_utils/facts/system/service_mgr.py:55-63
# asked: {"lines": [55, 56, 58, 61, 62, 63], "branches": [[58, 61], [58, 63], [61, 62], [61, 63]]}
# gained: {"lines": [55, 56, 58, 61, 62, 63], "branches": [[58, 61], [58, 63], [61, 62], [61, 63]]}

import os
import pytest
from unittest.mock import MagicMock, patch

# Assuming the ServiceMgrFactCollector class is imported from the module
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module():
    return MagicMock()

def test_is_systemd_managed_offline_systemctl_exists_and_is_symlink(mock_module, monkeypatch):
    # Mock the get_bin_path to return a valid path
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    
    # Mock os.path.islink to return True
    monkeypatch.setattr(os.path, 'islink', lambda x: x == '/sbin/init')
    
    # Mock os.readlink to return 'systemd'
    monkeypatch.setattr(os, 'readlink', lambda x: 'systemd' if x == '/sbin/init' else '')

    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == True

def test_is_systemd_managed_offline_systemctl_exists_and_not_symlink(mock_module, monkeypatch):
    # Mock the get_bin_path to return a valid path
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    
    # Mock os.path.islink to return False
    monkeypatch.setattr(os.path, 'islink', lambda x: False)
    
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == False

def test_is_systemd_managed_offline_systemctl_not_exists(mock_module):
    # Mock the get_bin_path to return None
    mock_module.get_bin_path.return_value = None
    
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == False
