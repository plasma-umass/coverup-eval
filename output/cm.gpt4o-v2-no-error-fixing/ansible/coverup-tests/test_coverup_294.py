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

def test_is_systemd_managed_offline_systemctl_present_and_symlink(mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    
    with patch('os.path.islink', return_value=True), \
         patch('os.readlink', return_value='systemd'):
        assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == True

def test_is_systemd_managed_offline_systemctl_present_but_not_symlink(mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    
    with patch('os.path.islink', return_value=False):
        assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == False

def test_is_systemd_managed_offline_systemctl_not_present(mock_module):
    mock_module.get_bin_path.return_value = None
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == False
