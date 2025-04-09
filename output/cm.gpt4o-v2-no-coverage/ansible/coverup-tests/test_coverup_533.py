# file: lib/ansible/modules/cron.py:428-433
# asked: {"lines": [428, 429, 430, 431, 433], "branches": [[429, 430], [429, 433], [430, 429], [430, 431]]}
# gained: {"lines": [428, 429, 430, 431, 433], "branches": [[429, 430], [429, 433], [430, 429], [430, 431]]}

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def cron_tab(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/usr/bin/crontab'
    module.run_command.return_value = (0, "", "")
    cron = CronTab(module)
    cron.lines = [
        "PATH=/usr/bin",
        "SHELL=/bin/bash",
        "MAILTO=root",
        "HOME=/"
    ]
    return cron

def test_find_env_exists(cron_tab):
    result = cron_tab.find_env("PATH")
    assert result == [0, "PATH=/usr/bin"]

def test_find_env_not_exists(cron_tab):
    result = cron_tab.find_env("NOTSET")
    assert result == []
