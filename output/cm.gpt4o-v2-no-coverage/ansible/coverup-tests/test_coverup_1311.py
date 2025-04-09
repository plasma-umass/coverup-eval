# file: lib/ansible/modules/cron.py:345-346
# asked: {"lines": [346], "branches": []}
# gained: {"lines": [346], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the CronTab class is imported from the ansible.modules.cron module
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    return module

@pytest.fixture
def cron_tab(mock_module):
    with patch('ansible.modules.cron.CronTab.read', return_value=None):
        return CronTab(mock_module)

def test_update_job(cron_tab, mocker):
    mocker.patch.object(cron_tab, '_update_job', return_value=True)
    mocker.patch.object(cron_tab, 'do_add_job')

    name = "test_job"
    job = "echo 'Hello World'"

    result = cron_tab.update_job(name, job)

    cron_tab._update_job.assert_called_once_with(name, job, cron_tab.do_add_job)
    assert result is True
