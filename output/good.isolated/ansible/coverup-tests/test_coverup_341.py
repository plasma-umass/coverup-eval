# file lib/ansible/modules/cron.py:293-300
# lines [293, 294, 295, 297, 298, 299, 300]
# branches ['294->295', '294->297', '297->298', '297->300', '298->297', '298->299']

import pytest
from unittest.mock import MagicMock
from ansible.modules.cron import CronTab

@pytest.fixture
def crontab():
    module = MagicMock()
    module.run_command.return_value = (0, '', '')  # Mock the run_command return value
    return CronTab(module)

def test_crontab_is_empty_with_no_lines(crontab):
    crontab.lines = []
    assert crontab.is_empty() == True

def test_crontab_is_empty_with_blank_lines(crontab):
    crontab.lines = ['   ', '\t', '\n']
    assert crontab.is_empty() == True

def test_crontab_is_not_empty_with_non_blank_line(crontab):
    crontab.lines = ['   ', '\t', '0 1 * * * /bin/true\n']
    assert crontab.is_empty() == False
