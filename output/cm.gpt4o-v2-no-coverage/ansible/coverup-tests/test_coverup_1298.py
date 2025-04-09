# file: lib/ansible/modules/cron.py:338-343
# asked: {"lines": [340, 343], "branches": []}
# gained: {"lines": [340, 343], "branches": []}

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/usr/bin/crontab'
    module.run_command.return_value = (0, '', '')
    return module

@pytest.fixture
def cron_tab(mock_module):
    return CronTab(module=mock_module)

def test_add_job(cron_tab, mocker):
    mocker.patch.object(cron_tab, 'do_comment', return_value='#Ansible: test_job')
    cron_tab.lines = []

    cron_tab.add_job('test_job', 'echo "Hello World"')

    assert cron_tab.lines == ['#Ansible: test_job', 'echo "Hello World"']
