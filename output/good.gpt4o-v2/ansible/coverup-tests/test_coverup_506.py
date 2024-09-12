# file: lib/ansible/modules/cron.py:391-399
# asked: {"lines": [391, 392, 393, 394, 395, 397, 398, 399], "branches": []}
# gained: {"lines": [391, 392, 393, 394, 395, 397, 398, 399], "branches": []}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.cron import CronTab, CronTabError

@pytest.fixture
def cron_tab():
    module = MagicMock()
    return CronTab(module, user='testuser', cron_file='/tmp/test_cron')

def test_remove_job_file_success(cron_tab):
    with patch('os.unlink') as mock_unlink:
        mock_unlink.return_value = None
        result = cron_tab.remove_job_file()
        assert result is True
        mock_unlink.assert_called_once_with('/tmp/test_cron')

def test_remove_job_file_oserror(cron_tab):
    with patch('os.unlink', side_effect=OSError):
        result = cron_tab.remove_job_file()
        assert result is False

def test_remove_job_file_unexpected_error(cron_tab):
    with patch('os.unlink', side_effect=Exception):
        with pytest.raises(CronTabError) as excinfo:
            cron_tab.remove_job_file()
        assert 'Unexpected error:' in str(excinfo.value)
