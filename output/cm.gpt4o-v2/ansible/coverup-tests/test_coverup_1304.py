# file: lib/ansible/modules/cron.py:379-380
# asked: {"lines": [380], "branches": []}
# gained: {"lines": [380], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming the CronTab class is imported from the module
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, "", ""))
    return module

@pytest.fixture
def crontab(mock_module):
    return CronTab(mock_module)

def test_update_env(crontab):
    name = "TEST_ENV"
    decl = "TEST_VALUE"
    
    # Mock the _update_env method to track its call
    crontab._update_env = MagicMock(return_value="mocked_result")
    
    result = crontab.update_env(name, decl)
    
    # Assert that _update_env was called with the correct parameters
    crontab._update_env.assert_called_once_with(name, decl, crontab.do_add_env)
    
    # Assert the result is as expected
    assert result == "mocked_result"
