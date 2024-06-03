# file lib/ansible/modules/cron.py:379-380
# lines [379, 380]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the CronTab class is imported from ansible.modules.cron
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_crontab(mocker):
    module = mocker.MagicMock()
    module.run_command = mocker.MagicMock(return_value=(0, '', ''))
    crontab = CronTab(module)
    crontab._update_env = mocker.MagicMock(return_value=True)
    crontab.do_add_env = mocker.MagicMock()
    return crontab

def test_update_env(mock_crontab):
    name = "TEST_ENV"
    decl = "value"
    
    result = mock_crontab.update_env(name, decl)
    
    mock_crontab._update_env.assert_called_once_with(name, decl, mock_crontab.do_add_env)
    assert result == True
