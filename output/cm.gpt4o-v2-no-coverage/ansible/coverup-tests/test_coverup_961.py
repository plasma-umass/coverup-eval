# file: lib/ansible/modules/cron.py:353-354
# asked: {"lines": [353, 354], "branches": []}
# gained: {"lines": [353, 354], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming the CronTab class is imported from the appropriate module
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    return module

@pytest.fixture
def crontab(mock_module):
    return CronTab(mock_module)

def test_remove_job(crontab, mocker):
    mocker.patch.object(crontab, '_update_job', return_value=True)
    result = crontab.remove_job('test_job')
    crontab._update_job.assert_called_once_with('test_job', '', crontab.do_remove_job)
    assert result is True
