# file lib/ansible/modules/cron.py:235-255
# lines [246, 247, 248, 250, 251]
# branches ['244->246', '246->247', '246->250']

import os
import pytest
from unittest import mock
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module():
    module = mock.Mock()
    module.get_bin_path.return_value = '/usr/bin/crontab'
    return module

def test_crontab_with_absolute_cron_file(mock_module):
    cron_file = '/tmp/test_cron'
    with mock.patch('os.path.isabs', return_value=True):
        cron_tab = CronTab(module=mock_module, cron_file=cron_file)
        assert cron_tab.cron_file == cron_file
        assert cron_tab.b_cron_file == cron_file.encode()

def test_crontab_with_relative_cron_file(mock_module):
    cron_file = 'test_cron'
    with mock.patch('os.path.isabs', return_value=False):
        cron_tab = CronTab(module=mock_module, cron_file=cron_file)
        assert cron_tab.cron_file == os.path.join('/etc/cron.d', cron_file)
        assert cron_tab.b_cron_file == os.path.join(b'/etc/cron.d', cron_file.encode())
