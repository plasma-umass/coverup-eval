# file: lib/ansible/module_utils/facts/system/service_mgr.py:43-53
# asked: {"lines": [43, 44, 46, 50, 51, 52, 53], "branches": [[46, 50], [46, 53], [50, 51], [50, 53], [51, 50], [51, 52]]}
# gained: {"lines": [43, 44, 46, 50, 51, 52, 53], "branches": [[46, 50], [46, 53], [50, 51], [50, 53], [51, 50], [51, 52]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module():
    module = MagicMock()
    return module

def test_is_systemd_managed_systemctl_not_found(mock_module):
    mock_module.get_bin_path.return_value = None
    assert not ServiceMgrFactCollector.is_systemd_managed(mock_module)

def test_is_systemd_managed_canary_found(mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    with patch('os.path.exists', side_effect=lambda path: path == '/run/systemd/system/'):
        assert ServiceMgrFactCollector.is_systemd_managed(mock_module)

def test_is_systemd_managed_no_canary_found(mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    with patch('os.path.exists', return_value=False):
        assert not ServiceMgrFactCollector.is_systemd_managed(mock_module)
