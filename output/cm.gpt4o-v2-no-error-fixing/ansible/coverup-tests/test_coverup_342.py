# file: lib/ansible/cli/playbook.py:213-217
# asked: {"lines": [213, 214, 215, 216, 217], "branches": [[215, 0], [215, 216]]}
# gained: {"lines": [213, 214, 215, 216, 217], "branches": [[215, 0], [215, 216]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.playbook import PlaybookCLI

@pytest.fixture
def mock_inventory():
    inventory = MagicMock()
    host1 = MagicMock()
    host2 = MagicMock()
    host1.get_name.return_value = 'host1'
    host2.get_name.return_value = 'host2'
    inventory.list_hosts.return_value = [host1, host2]
    return inventory

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

def test_flush_cache(mock_inventory, mock_variable_manager):
    PlaybookCLI._flush_cache(mock_inventory, mock_variable_manager)
    
    hosts = mock_inventory.list_hosts()
    assert mock_inventory.list_hosts.called
    assert mock_variable_manager.clear_facts.call_count == len(hosts)
    for host in hosts:
        hostname = host.get_name()
        mock_variable_manager.clear_facts.assert_any_call(hostname)
