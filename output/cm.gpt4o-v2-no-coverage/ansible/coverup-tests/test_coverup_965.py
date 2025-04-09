# file: lib/ansible/modules/cron.py:356-357
# asked: {"lines": [356, 357], "branches": []}
# gained: {"lines": [356, 357], "branches": []}

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.Mock()
    mock_module.get_bin_path.return_value = "/usr/bin/crontab"
    mock_module.run_command.return_value = (0, "", "")
    return mock_module

def test_do_remove_job(mock_module):
    crontab = CronTab(mock_module)
    lines = ["* * * * * /path/to/command #Ansible: test"]
    comment = "#Ansible: test"
    job = "* * * * * /path/to/command"
    
    result = crontab.do_remove_job(lines, comment, job)
    
    assert result is None
