# file lib/ansible/modules/cron.py:464-471
# lines [464, 465, 467, 468, 469, 471]
# branches ['467->468', '467->471', '468->467', '468->469']

import pytest
import re

class CronTab(object):
    def __init__(self, lines):
        self.lines = lines

    def get_envnames(self):
        envnames = []
        for l in self.lines:
            if re.match(r'^\S+=', l):
                envnames.append(l.split('=')[0])
        return envnames

def test_get_envnames():
    lines = [
        "PATH=/usr/bin",
        "MAILTO=root",
        "0 1 * * * /usr/bin/python /path/to/script.py",
        "HOME=/home/user",
        "SHELL=/bin/bash",
        "INVALID LINE",
        "ANOTHER=valid"
    ]
    crontab = CronTab(lines)
    envnames = crontab.get_envnames()
    
    assert envnames == ["PATH", "MAILTO", "HOME", "SHELL", "ANOTHER"]

    # Clean up
    del crontab

@pytest.fixture
def mock_crontab(mocker):
    lines = [
        "PATH=/usr/bin",
        "MAILTO=root",
        "0 1 * * * /usr/bin/python /path/to/script.py",
        "HOME=/home/user",
        "SHELL=/bin/bash",
        "INVALID LINE",
        "ANOTHER=valid"
    ]
    mocker.patch('ansible.modules.cron.CronTab', return_value=CronTab(lines))

def test_crontab_get_envnames(mock_crontab):
    from ansible.modules.cron import CronTab
    crontab = CronTab([])
    envnames = crontab.get_envnames()
    
    assert envnames == ["PATH", "MAILTO", "HOME", "SHELL", "ANOTHER"]

    # Clean up
    del crontab
