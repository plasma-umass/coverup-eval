# file lib/ansible/module_utils/facts/system/service_mgr.py:55-63
# lines [55, 56, 58, 61, 62, 63]
# branches ['58->61', '58->63', '61->62', '61->63']

import os
import pytest
from unittest.mock import patch, MagicMock

from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path = MagicMock(return_value='/bin/systemctl')
    return module

def test_is_systemd_managed_offline_systemctl_present(mock_module):
    with patch('os.path.islink', return_value=True), \
         patch('os.readlink', return_value='/lib/systemd/systemd'):
        assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == True

def test_is_systemd_managed_offline_systemctl_absent(mock_module):
    mock_module.get_bin_path = MagicMock(return_value=None)
    assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == False

def test_is_systemd_managed_offline_init_not_symlink(mock_module):
    with patch('os.path.islink', return_value=False):
        assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == False

def test_is_systemd_managed_offline_init_not_systemd(mock_module):
    with patch('os.path.islink', return_value=True), \
         patch('os.readlink', return_value='/sbin/init'):
        assert ServiceMgrFactCollector.is_systemd_managed_offline(mock_module) == False
