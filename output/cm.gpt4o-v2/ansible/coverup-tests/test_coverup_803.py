# file: lib/ansible/modules/cron.py:348-351
# asked: {"lines": [348, 349, 351], "branches": []}
# gained: {"lines": [348, 349, 351], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.modules.cron import CronTab

def test_do_add_job():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/crontab')
    module.run_command = Mock(return_value=(0, '', ''))
    cron = CronTab(module=module)
    lines = []
    comment = "#Ansible: test job"
    job = "echo 'Hello World'"

    cron.do_add_job(lines, comment, job)

    assert lines == [comment, job]
