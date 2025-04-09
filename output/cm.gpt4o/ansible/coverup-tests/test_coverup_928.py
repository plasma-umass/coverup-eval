# file lib/ansible/modules/cron.py:385-386
# lines [385, 386]
# branches []

import pytest
from unittest import mock

# Assuming the CronTab class is imported from ansible.modules.cron
from ansible.modules.cron import CronTab

@pytest.fixture
def crontab(mocker):
    # Mock the module argument required by CronTab
    mock_module = mocker.Mock()
    # Mock the run_command method to return a tuple
    mock_module.run_command.return_value = (0, '', '')
    return CronTab(mock_module)

def test_remove_env(mocker, crontab):
    # Mock the _update_env method
    mock_update_env = mocker.patch.object(crontab, '_update_env', return_value=True)
    
    # Call the remove_env method
    result = crontab.remove_env('TEST_ENV')
    
    # Assert that _update_env was called with the correct parameters
    mock_update_env.assert_called_once_with('TEST_ENV', '', crontab.do_remove_env)
    
    # Assert the result is as expected
    assert result == True
