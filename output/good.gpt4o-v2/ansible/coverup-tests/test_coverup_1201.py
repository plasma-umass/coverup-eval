# file: lib/ansible/modules/cron.py:455-462
# asked: {"lines": [456, 458, 459, 460, 462], "branches": [[458, 459], [458, 462], [459, 458], [459, 460]]}
# gained: {"lines": [456, 458, 459, 460, 462], "branches": [[458, 459], [458, 462], [459, 458], [459, 460]]}

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/usr/bin/crontab'
    module.run_command.return_value = (0, '', '')
    return module

def test_get_jobnames(mocker, mock_module):
    cron = CronTab(module=mock_module)
    cron.lines = [
        '#Ansible: job1',
        '#Ansible: job2',
        'some other line'
    ]
    
    jobnames = cron.get_jobnames()
    
    assert jobnames == ['job1', 'job2']

    # Clean up
    cron.lines = []
