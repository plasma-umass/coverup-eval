# file: lib/ansible/modules/cron.py:388-389
# asked: {"lines": [388, 389], "branches": []}
# gained: {"lines": [388, 389], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/crontab')
    module.run_command = Mock(return_value=(0, '', ''))
    return module

def test_do_remove_env(mock_module):
    with patch('ansible.modules.cron.CronTab.read', return_value=None):
        crontab = CronTab(mock_module)
        lines = ["PATH=/usr/bin", "SHELL=/bin/bash"]
        decl = "PATH"
        
        result = crontab.do_remove_env(lines, decl)
        
        assert result is None
