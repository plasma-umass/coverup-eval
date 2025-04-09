# file: lib/ansible/modules/cron.py:388-389
# asked: {"lines": [388, 389], "branches": []}
# gained: {"lines": [388, 389], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.modules.cron import CronTab

def test_do_remove_env():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/crontab')
    module.run_command = Mock(return_value=(0, '', ''))
    cron_tab = CronTab(module)
    lines = ["PATH=/usr/bin", "SHELL=/bin/bash"]
    decl = "PATH"
    
    result = cron_tab.do_remove_env(lines, decl)
    
    assert result is None
