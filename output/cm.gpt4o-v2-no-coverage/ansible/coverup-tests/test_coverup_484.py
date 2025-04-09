# file: lib/ansible/modules/cron.py:494-503
# asked: {"lines": [494, 495, 497, 498, 499, 501, 503], "branches": [[497, 498], [497, 503], [498, 499], [498, 501]]}
# gained: {"lines": [494, 495, 497, 498, 499, 501, 503], "branches": [[497, 498], [497, 503], [498, 499], [498, 501]]}

import pytest
from unittest.mock import Mock, patch
from ansible.modules.cron import CronTab

@pytest.fixture
def cron_tab():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/crontab')
    module.run_command = Mock(return_value=(0, "", ""))
    with patch('ansible.modules.cron.to_native', side_effect=lambda x, errors='strict': x.decode(errors)):
        return CronTab(module)

def test_update_env_adds_new_env_variable(cron_tab):
    cron_tab.lines = ["PATH=/usr/bin", "HOME=/home/user"]
    def addenvfunction(newlines, decl):
        newlines.append(decl)
    
    cron_tab._update_env("NEW_VAR", "NEW_VAR=value", addenvfunction)
    
    assert "NEW_VAR=value" not in cron_tab.lines
    assert len(cron_tab.lines) == 2

def test_update_env_updates_existing_env_variable(cron_tab):
    cron_tab.lines = ["PATH=/usr/bin", "HOME=/home/user"]
    def addenvfunction(newlines, decl):
        newlines.append(decl)
    
    cron_tab._update_env("PATH", "PATH=/usr/local/bin", addenvfunction)
    
    assert "PATH=/usr/local/bin" in cron_tab.lines
    assert "PATH=/usr/bin" not in cron_tab.lines
    assert len(cron_tab.lines) == 2

def test_update_env_no_matching_env_variable(cron_tab):
    cron_tab.lines = ["PATH=/usr/bin", "HOME=/home/user"]
    def addenvfunction(newlines, decl):
        newlines.append(decl)
    
    cron_tab._update_env("NOT_EXIST", "NOT_EXIST=value", addenvfunction)
    
    assert "NOT_EXIST=value" not in cron_tab.lines
    assert len(cron_tab.lines) == 2
