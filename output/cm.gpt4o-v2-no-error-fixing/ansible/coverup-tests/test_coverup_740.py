# file: lib/ansible/modules/cron.py:235-255
# asked: {"lines": [235, 236, 237, 238, 239, 240, 241, 242, 244, 246, 247, 248, 250, 251, 253, 255], "branches": [[244, 246], [244, 253], [246, 247], [246, 250]]}
# gained: {"lines": [235, 236, 237, 238, 239, 240, 241, 242, 244, 246, 247, 248, 250, 251, 253, 255], "branches": [[244, 246], [244, 253], [246, 247], [246, 250]]}

import os
import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.module_utils.common.text.converters import to_bytes
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module():
    module = MagicMock(spec=AnsibleModule)
    module.get_bin_path.return_value = '/usr/bin/crontab'
    return module

def test_crontab_init_with_absolute_cron_file(mock_module):
    cron_file = '/etc/cron.d/test_cron'
    with patch('os.path.isabs', return_value=True), \
         patch('ansible.modules.cron.to_bytes', return_value=b'/etc/cron.d/test_cron'), \
         patch('builtins.open', mock_open(read_data=b'')), \
         patch('os.getuid', return_value=0):
        cron = CronTab(mock_module, cron_file=cron_file)
        assert cron.cron_file == cron_file
        assert cron.b_cron_file == b'/etc/cron.d/test_cron'
        assert cron.lines == []

def test_crontab_init_with_relative_cron_file(mock_module):
    cron_file = 'test_cron'
    with patch('os.path.isabs', return_value=False), \
         patch('ansible.modules.cron.to_bytes', return_value=b'test_cron'), \
         patch('builtins.open', mock_open(read_data=b'')), \
         patch('os.getuid', return_value=0):
        cron = CronTab(mock_module, cron_file=cron_file)
        assert cron.cron_file == '/etc/cron.d/test_cron'
        assert cron.b_cron_file == b'/etc/cron.d/test_cron'
        assert cron.lines == []

def test_crontab_init_without_cron_file(mock_module):
    with patch('os.getuid', return_value=0), \
         patch.object(CronTab, 'read', return_value=None):
        cron = CronTab(mock_module)
        assert cron.cron_file is None
        assert cron.lines is None
