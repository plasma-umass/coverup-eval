# file: lib/ansible/executor/playbook_executor.py:321-336
# asked: {"lines": [327, 328, 329, 330, 331, 332, 333, 334, 336], "branches": [[330, 331], [330, 336]]}
# gained: {"lines": [327, 328, 329, 330, 331, 332, 333, 334, 336], "branches": [[330, 331], [330, 336]]}

import pytest
import os
from unittest.mock import patch, mock_open
from ansible.executor.playbook_executor import PlaybookExecutor

@pytest.fixture
def playbook_executor():
    return PlaybookExecutor([], None, None, None, None)

def test_generate_retry_inventory_success(playbook_executor):
    retry_path = '/tmp/retry_inventory'
    replay_hosts = ['host1', 'host2']

    with patch('ansible.executor.playbook_executor.makedirs_safe') as mock_makedirs_safe, \
         patch('builtins.open', mock_open()) as mock_file:
        result = playbook_executor._generate_retry_inventory(retry_path, replay_hosts)
        mock_makedirs_safe.assert_called_once_with(os.path.dirname(retry_path))
        mock_file.assert_called_once_with(retry_path, 'w')
        mock_file().write.assert_any_call("host1\n")
        mock_file().write.assert_any_call("host2\n")
        assert result is True

def test_generate_retry_inventory_failure(playbook_executor):
    retry_path = '/tmp/retry_inventory'
    replay_hosts = ['host1', 'host2']

    with patch('ansible.executor.playbook_executor.makedirs_safe', side_effect=Exception('error')), \
         patch('ansible.executor.playbook_executor.display') as mock_display:
        result = playbook_executor._generate_retry_inventory(retry_path, replay_hosts)
        mock_display.warning.assert_called_once_with("Could not create retry file '/tmp/retry_inventory'.\n\terror")
        assert result is False
