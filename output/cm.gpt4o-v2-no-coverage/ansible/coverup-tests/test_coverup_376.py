# file: lib/ansible/module_utils/facts/system/service_mgr.py:43-53
# asked: {"lines": [43, 44, 46, 50, 51, 52, 53], "branches": [[46, 50], [46, 53], [50, 51], [50, 53], [51, 50], [51, 52]]}
# gained: {"lines": [43, 44, 46, 50, 51, 52, 53], "branches": [[46, 50], [46, 53], [50, 51], [50, 53], [51, 50], [51, 52]]}

import os
import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_is_systemd_managed_with_systemctl_and_canary(mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    with patch('os.path.exists', return_value=True):
        assert ServiceMgrFactCollector.is_systemd_managed(mock_module) is True

def test_is_systemd_managed_with_systemctl_no_canary(mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    with patch('os.path.exists', return_value=False):
        assert ServiceMgrFactCollector.is_systemd_managed(mock_module) is False

def test_is_systemd_managed_without_systemctl(mock_module):
    mock_module.get_bin_path.return_value = None
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) is False
