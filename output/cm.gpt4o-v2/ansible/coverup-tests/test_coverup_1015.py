# file: lib/ansible/modules/cron.py:385-386
# asked: {"lines": [385, 386], "branches": []}
# gained: {"lines": [385, 386], "branches": []}

import pytest
from ansible.modules.cron import CronTab
from unittest.mock import Mock

@pytest.fixture
def cron_tab(mocker):
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/crontab')
    module.run_command = Mock(return_value=(0, '', ''))
    return CronTab(module)

def test_remove_env(cron_tab, mocker):
    # Setup initial state
    cron_tab.lines = ["TEST_ENV=value", "OTHER_ENV=othervalue"]
    
    # Mock the _update_env method to track its calls
    mock_update_env = mocker.patch.object(cron_tab, '_update_env', wraps=cron_tab._update_env)
    
    # Call the method under test
    cron_tab.remove_env("TEST_ENV")
    
    # Verify that _update_env was called with the correct parameters
    mock_update_env.assert_called_once_with("TEST_ENV", '', cron_tab.do_remove_env)
    
    # Verify the postconditions
    assert cron_tab.lines == ["OTHER_ENV=othervalue"]

def test_update_env(cron_tab):
    # Setup initial state
    cron_tab.lines = ["TEST_ENV=value", "OTHER_ENV=othervalue"]
    
    # Call the method under test
    cron_tab._update_env("TEST_ENV", '', cron_tab.do_remove_env)
    
    # Verify the postconditions
    assert cron_tab.lines == ["OTHER_ENV=othervalue"]
