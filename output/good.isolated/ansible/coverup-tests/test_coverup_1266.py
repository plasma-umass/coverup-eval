# file lib/ansible/module_utils/facts/system/service_mgr.py:43-53
# lines [46, 50, 51, 52, 53]
# branches ['46->50', '46->53', '50->51', '50->53', '51->50', '51->52']

import os
import pytest
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
from unittest.mock import call

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    return mock_module

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

def test_is_systemd_managed_true(mock_module, mock_os_path_exists):
    mock_os_path_exists.return_value = True
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) is True
    mock_os_path_exists.assert_called_once_with("/run/systemd/system/")

def test_is_systemd_managed_false_no_systemctl(mock_module, mock_os_path_exists):
    mock_module.get_bin_path.return_value = None
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) is False
    mock_os_path_exists.assert_not_called()

def test_is_systemd_managed_false_no_canary(mock_module, mock_os_path_exists):
    mock_os_path_exists.side_effect = lambda x: False
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) is False
    mock_os_path_exists.assert_has_calls([
        call("/run/systemd/system/"),
        call("/dev/.run/systemd/"),
        call("/dev/.systemd/")
    ])
