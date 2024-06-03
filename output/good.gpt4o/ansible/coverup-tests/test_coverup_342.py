# file lib/ansible/module_utils/facts/system/service_mgr.py:43-53
# lines [43, 44, 46, 50, 51, 52, 53]
# branches ['46->50', '46->53', '50->51', '50->53', '51->50', '51->52']

import os
import pytest
from unittest.mock import patch, MagicMock

# Assuming the ServiceMgrFactCollector class is defined in ansible.module_utils.facts.system.service_mgr
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module(mocker):
    module = MagicMock()
    mocker.patch.object(module, 'get_bin_path', return_value='/bin/systemctl')
    return module

def test_is_systemd_managed_systemctl_present(mock_module, mocker):
    # Mock os.path.exists to return True for the first canary path
    mocker.patch('os.path.exists', side_effect=lambda path: path == "/run/systemd/system/")
    
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == True

def test_is_systemd_managed_no_systemctl(mock_module, mocker):
    # Mock get_bin_path to return None, simulating systemctl not being present
    mock_module.get_bin_path.return_value = None
    
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == False

def test_is_systemd_managed_no_canary_paths(mock_module, mocker):
    # Mock os.path.exists to return False for all canary paths
    mocker.patch('os.path.exists', return_value=False)
    
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == False
