# file lib/ansible/modules/cron.py:348-351
# lines [349, 351]
# branches []

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_crontab(mocker):
    module_mock = mocker.Mock()
    module_mock.run_command.return_value = (0, '', '')
    return CronTab(module=module_mock)

def test_do_add_job(mock_crontab):
    lines = []
    comment = "# This is a comment"
    job = "0 5 * * * /usr/bin/somejob"

    mock_crontab.do_add_job(lines, comment, job)

    assert comment in lines
    assert job in lines

    # Clean up
    lines.clear()
