# file lib/ansible/modules/cron.py:348-351
# lines [348, 349, 351]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.modules.cron import CronTab

# Mocking the module parameter and the run_command method required by CronTab.__init__()
@pytest.fixture
def cron_tab(mocker):
    module_mock = MagicMock()
    module_mock.run_command = MagicMock(return_value=(0, '', ''))
    return CronTab(module_mock)

def test_do_add_job(cron_tab):
    lines = []
    comment = "#Ansible: Test job comment"
    job = "* * * * * /usr/bin/echo 'Hello, World!'"

    cron_tab.do_add_job(lines, comment, job)

    assert lines == [comment, job], "Job and comment should be added to lines"

# No cleanup code is necessary for this test as we are not interacting with the actual crontab.
