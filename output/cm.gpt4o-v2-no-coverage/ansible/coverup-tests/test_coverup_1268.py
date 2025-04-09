# file: lib/ansible/modules/cron.py:464-471
# asked: {"lines": [465, 467, 468, 469, 471], "branches": [[467, 468], [467, 471], [468, 467], [468, 469]]}
# gained: {"lines": [465, 467, 468, 469, 471], "branches": [[467, 468], [467, 471], [468, 467], [468, 469]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_crontab():
    module = MagicMock()
    with patch.object(CronTab, 'read', return_value=None):
        cron_tab = CronTab(module)
    return cron_tab

def test_get_envnames(mock_crontab):
    # Mock the 'lines' attribute with different test cases
    mock_crontab.lines = [
        "PATH=/usr/bin",
        "MAILTO=root",
        "0 5 * * * /usr/bin/find",
        "SHELL=/bin/bash"
    ]
    
    expected_envnames = ["PATH", "MAILTO", "SHELL"]
    
    # Call the method
    result = mock_crontab.get_envnames()
    
    # Assert the result
    assert result == expected_envnames

    # Clean up
    mock_crontab.lines = []

def test_get_envnames_no_env_vars(mock_crontab):
    # Mock the 'lines' attribute with no environment variables
    mock_crontab.lines = [
        "0 5 * * * /usr/bin/find",
        "0 6 * * * /usr/bin/updatedb"
    ]
    
    expected_envnames = []
    
    # Call the method
    result = mock_crontab.get_envnames()
    
    # Assert the result
    assert result == expected_envnames

    # Clean up
    mock_crontab.lines = []

def test_get_envnames_mixed_lines(mock_crontab):
    # Mock the 'lines' attribute with mixed lines
    mock_crontab.lines = [
        "PATH=/usr/bin",
        "0 5 * * * /usr/bin/find",
        "MAILTO=root",
        "0 6 * * * /usr/bin/updatedb",
        "SHELL=/bin/bash"
    ]
    
    expected_envnames = ["PATH", "MAILTO", "SHELL"]
    
    # Call the method
    result = mock_crontab.get_envnames()
    
    # Assert the result
    assert result == expected_envnames

    # Clean up
    mock_crontab.lines = []

