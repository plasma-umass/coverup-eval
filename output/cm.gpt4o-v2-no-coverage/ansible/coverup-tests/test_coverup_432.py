# file: lib/ansible/executor/playbook_executor.py:321-336
# asked: {"lines": [321, 327, 328, 329, 330, 331, 332, 333, 334, 336], "branches": [[330, 331], [330, 336]]}
# gained: {"lines": [321, 327, 328, 329, 330, 331, 332, 333, 334, 336], "branches": [[330, 331], [330, 336]]}

import pytest
import os
from unittest.mock import patch, mock_open, MagicMock
from ansible.executor.playbook_executor import PlaybookExecutor

@pytest.fixture
def playbook_executor():
    playbooks = ['dummy_playbook.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = MagicMock()
    return PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

def test_generate_retry_inventory_success(playbook_executor):
    retry_path = '/tmp/retry_inventory'
    replay_hosts = ['host1', 'host2', 'host3']

    with patch('ansible.executor.playbook_executor.makedirs_safe') as mock_makedirs_safe, \
         patch('builtins.open', mock_open()) as mock_file:
        result = playbook_executor._generate_retry_inventory(retry_path, replay_hosts)
        
        mock_makedirs_safe.assert_called_once_with(os.path.dirname(retry_path))
        mock_file.assert_called_once_with(retry_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('host1\n')
        handle.write.assert_any_call('host2\n')
        handle.write.assert_any_call('host3\n')
        
        assert result is True

def test_generate_retry_inventory_failure(playbook_executor):
    retry_path = '/tmp/retry_inventory'
    replay_hosts = ['host1', 'host2', 'host3']

    with patch('ansible.executor.playbook_executor.makedirs_safe', side_effect=Exception('makedirs error')), \
         patch('ansible.executor.playbook_executor.to_text', return_value='makedirs error'), \
         patch('ansible.executor.playbook_executor.display.warning') as mock_warning:
        result = playbook_executor._generate_retry_inventory(retry_path, replay_hosts)
        
        mock_warning.assert_called_once_with("Could not create retry file '/tmp/retry_inventory'.\n\tmakedirs error")
        assert result is False

def test_generate_retry_inventory_open_failure(playbook_executor):
    retry_path = '/tmp/retry_inventory'
    replay_hosts = ['host1', 'host2', 'host3']

    with patch('ansible.executor.playbook_executor.makedirs_safe'), \
         patch('builtins.open', mock_open()) as mock_file, \
         patch('ansible.executor.playbook_executor.to_text', return_value='open error'), \
         patch('ansible.executor.playbook_executor.display.warning') as mock_warning:
        mock_file.side_effect = Exception('open error')
        result = playbook_executor._generate_retry_inventory(retry_path, replay_hosts)
        
        mock_warning.assert_called_once_with("Could not create retry file '/tmp/retry_inventory'.\n\topen error")
        assert result is False
