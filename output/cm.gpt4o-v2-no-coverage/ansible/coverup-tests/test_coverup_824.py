# file: lib/ansible/modules/cron.py:348-351
# asked: {"lines": [348, 349, 351], "branches": []}
# gained: {"lines": [348, 349, 351], "branches": []}

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def cron_tab(mocker):
    class MockModule:
        def get_bin_path(self, arg, required):
            return "/usr/bin/crontab"
        
        def run_command(self, command, use_unsafe_shell):
            return (0, "", "")
    
    return CronTab(MockModule())

def test_do_add_job(cron_tab):
    lines = []
    comment = "# Test comment"
    job = "echo 'Hello World'"
    
    cron_tab.do_add_job(lines, comment, job)
    
    assert lines == [comment, job]
