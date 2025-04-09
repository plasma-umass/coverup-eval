# file: lib/ansible/modules/cron.py:379-380
# asked: {"lines": [379, 380], "branches": []}
# gained: {"lines": [379, 380], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/bin/crontab'
    module.run_command.return_value = (0, '', '')
    return module

@pytest.fixture
def crontab(mock_module):
    with patch('ansible.modules.cron.CronTab.read', return_value=None):
        return CronTab(mock_module)

def test_update_env(crontab, mocker):
    mocker.patch.object(crontab, '_update_env', return_value=True)
    mocker.patch.object(crontab, 'do_add_env', return_value=True)
    
    name = 'TEST_ENV'
    decl = 'TEST_VALUE'
    
    result = crontab.update_env(name, decl)
    
    crontab._update_env.assert_called_once_with(name, decl, crontab.do_add_env)
    assert result is True
