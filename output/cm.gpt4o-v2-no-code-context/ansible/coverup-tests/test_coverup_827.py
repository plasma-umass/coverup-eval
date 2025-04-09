# file: lib/ansible/modules/cron.py:356-357
# asked: {"lines": [356, 357], "branches": []}
# gained: {"lines": [356, 357], "branches": []}

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def cron_tab(mocker):
    module_mock = mocker.Mock()
    module_mock.run_command.return_value = (0, "", "")
    return CronTab(module=module_mock)

def test_do_remove_job(cron_tab):
    lines = ["* * * * * /path/to/command # comment"]
    comment = "comment"
    job = "* * * * * /path/to/command"
    
    result = cron_tab.do_remove_job(lines, comment, job)
    
    assert result is None
