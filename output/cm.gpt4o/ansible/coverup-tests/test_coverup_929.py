# file lib/ansible/modules/cron.py:382-383
# lines [382, 383]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the CronTab class is imported from ansible.modules.cron
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_crontab():
    module_mock = MagicMock()
    module_mock.run_command.return_value = (0, '', '')  # Mock the return value of run_command
    crontab = CronTab(module=module_mock)
    crontab.cron_file = None  # Ensure cron_file is None to avoid file operations
    return crontab

def test_do_add_env(mock_crontab):
    lines = []
    decl = "SHELL=/bin/bash"
    
    mock_crontab.do_add_env(lines, decl)
    
    assert len(lines) == 1
    assert lines[0] == decl

    # Clean up
    lines.clear()
    assert len(lines) == 0
