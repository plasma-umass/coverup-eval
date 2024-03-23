# file lib/ansible/module_utils/facts/system/service_mgr.py:55-63
# lines [55, 56, 58, 61, 62, 63]
# branches ['58->61', '58->63', '61->62', '61->63']

import os
import pytest
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

# Mock for os.path.islink and os.readlink
def mock_islink(path):
    if path == '/sbin/init':
        return True
    return False

def mock_readlink(path):
    if path == '/sbin/init':
        return '/lib/systemd/systemd'
    return ''

# Mock for module.get_bin_path
def mock_get_bin_path(bin_name):
    if bin_name == 'systemctl':
        return '/bin/systemctl'
    return None

@pytest.fixture
def mock_module(mocker):
    mock = mocker.MagicMock()
    mock.get_bin_path.side_effect = mock_get_bin_path
    return mock

def test_is_systemd_managed_offline_true(mock_module, mocker):
    mocker.patch('os.path.islink', side_effect=mock_islink)
    mocker.patch('os.readlink', side_effect=mock_readlink)
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) is True

def test_is_systemd_managed_offline_false_no_systemctl(mock_module, mocker):
    mocker.patch('os.path.islink', side_effect=mock_islink)
    mocker.patch('os.readlink', side_effect=mock_readlink)
    mock_module.get_bin_path.side_effect = lambda bin_name: None
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) is False

def test_is_systemd_managed_offline_false_no_symlink(mock_module, mocker):
    mocker.patch('os.path.islink', return_value=False)
    mocker.patch('os.readlink', return_value='')
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) is False

def test_is_systemd_managed_offline_false_wrong_symlink(mock_module, mocker):
    mocker.patch('os.path.islink', side_effect=mock_islink)
    mocker.patch('os.readlink', return_value='/lib/init/upstart')
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) is False
