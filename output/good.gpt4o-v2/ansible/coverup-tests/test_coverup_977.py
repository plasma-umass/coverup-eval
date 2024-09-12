# file: lib/ansible/modules/cron.py:335-336
# asked: {"lines": [335, 336], "branches": []}
# gained: {"lines": [335, 336], "branches": []}

import pytest
from ansible.modules.cron import CronTab

def test_do_comment(mocker):
    class MockModule:
        def get_bin_path(self, arg, required):
            return "/usr/bin/crontab"
        
        def run_command(self, command, use_unsafe_shell):
            return (0, "", "")

    module = MockModule()
    cron = CronTab(module)
    
    result = cron.do_comment("test_name")
    assert result == "#Ansible: test_name"
