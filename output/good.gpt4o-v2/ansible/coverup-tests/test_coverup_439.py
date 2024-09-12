# file: lib/ansible/module_utils/facts/system/service_mgr.py:55-63
# asked: {"lines": [55, 56, 58, 61, 62, 63], "branches": [[58, 61], [58, 63], [61, 62], [61, 63]]}
# gained: {"lines": [55, 56, 58, 61, 62, 63], "branches": [[58, 61], [58, 63], [61, 62], [61, 63]]}

import os
import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_is_systemd_managed_offline_systemctl_not_found(mock_module):
    mock_module.get_bin_path.return_value = None
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(mock_module)

@patch('os.path.islink')
@patch('os.readlink')
def test_is_systemd_managed_offline_systemd_link(mock_readlink, mock_islink, mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    mock_islink.return_value = True
    mock_readlink.return_value = 'systemd'
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module)

@patch('os.path.islink')
@patch('os.readlink')
def test_is_systemd_managed_offline_not_systemd_link(mock_readlink, mock_islink, mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    mock_islink.return_value = True
    mock_readlink.return_value = 'not_systemd'
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(mock_module)

@patch('os.path.islink')
def test_is_systemd_managed_offline_no_symlink(mock_islink, mock_module):
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    mock_islink.return_value = False
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(mock_module)
