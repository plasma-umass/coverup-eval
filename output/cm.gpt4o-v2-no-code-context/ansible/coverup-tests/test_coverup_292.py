# file: lib/ansible/module_utils/facts/system/service_mgr.py:43-53
# asked: {"lines": [43, 44, 46, 50, 51, 52, 53], "branches": [[46, 50], [46, 53], [50, 51], [50, 53], [51, 50], [51, 52]]}
# gained: {"lines": [43, 44, 46, 50, 51, 52, 53], "branches": [[46, 50], [46, 53], [50, 51], [50, 53], [51, 50], [51, 52]]}

import os
import pytest
from unittest.mock import MagicMock, patch

# Assuming the ServiceMgrFactCollector class is imported from the module
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module():
    return MagicMock()

def test_is_systemd_managed_systemctl_found_canary_exists(mock_module, monkeypatch):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    
    def mock_exists(path):
        return path == "/run/systemd/system/"
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == True

def test_is_systemd_managed_systemctl_found_no_canary_exists(mock_module, monkeypatch):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    
    def mock_exists(path):
        return False
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == False

def test_is_systemd_managed_systemctl_not_found(mock_module):
    mock_module.get_bin_path.return_value = None
    
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == False
