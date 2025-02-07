# file: lib/ansible/modules/cron.py:382-383
# asked: {"lines": [382, 383], "branches": []}
# gained: {"lines": [382, 383], "branches": []}

import pytest
from ansible.modules.cron import CronTab
from unittest.mock import Mock

def test_do_add_env():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/crontab')
    module.run_command = Mock(return_value=(0, '', ''))
    crontab = CronTab(module)
    lines = []
    decl = "TEST_ENV=1"
    
    crontab.do_add_env(lines, decl)
    
    assert decl in lines
