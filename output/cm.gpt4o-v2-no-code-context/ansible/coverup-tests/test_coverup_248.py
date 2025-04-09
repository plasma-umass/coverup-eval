# file: lib/ansible/plugins/lookup/inventory_hostnames.py:42-53
# asked: {"lines": [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53], "branches": [[45, 46], [45, 50], [47, 45], [47, 48]]}
# gained: {"lines": [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53], "branches": [[45, 46], [45, 50], [47, 45], [47, 48]]}

import pytest
from ansible.plugins.lookup.inventory_hostnames import LookupModule
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_loader():
    return MagicMock(spec=DataLoader)

@pytest.fixture
def mock_inventory_manager():
    with patch('ansible.plugins.lookup.inventory_hostnames.InventoryManager') as mock:
        yield mock

def test_run_with_valid_terms(mock_loader, mock_inventory_manager):
    lookup = LookupModule(mock_loader, None)
    terms = 'all'
    variables = {
        'groups': {
            'group1': ['host1', 'host2'],
            'group2': ['host3']
        }
    }
    
    mock_manager_instance = mock_inventory_manager.return_value
    mock_host1 = MagicMock()
    mock_host1.name = 'host1'
    mock_host2 = MagicMock()
    mock_host2.name = 'host2'
    mock_host3 = MagicMock()
    mock_host3.name = 'host3'
    mock_manager_instance.get_hosts.return_value = [mock_host1, mock_host2, mock_host3]

    result = lookup.run(terms, variables)
    
    mock_inventory_manager.assert_called_once_with(mock_loader, parse=False)
    mock_manager_instance.add_group.assert_any_call('group1')
    mock_manager_instance.add_group.assert_any_call('group2')
    mock_manager_instance.add_host.assert_any_call('host1', group='group1')
    mock_manager_instance.add_host.assert_any_call('host2', group='group1')
    mock_manager_instance.add_host.assert_any_call('host3', group='group2')
    mock_manager_instance.get_hosts.assert_called_once_with(pattern=terms)
    
    assert result == ['host1', 'host2', 'host3']

def test_run_with_ansible_error(mock_loader, mock_inventory_manager):
    lookup = LookupModule(mock_loader, None)
    terms = 'all'
    variables = {
        'groups': {
            'group1': ['host1', 'host2'],
            'group2': ['host3']
        }
    }
    
    mock_manager_instance = mock_inventory_manager.return_value
    mock_manager_instance.get_hosts.side_effect = AnsibleError

    result = lookup.run(terms, variables)
    
    mock_inventory_manager.assert_called_once_with(mock_loader, parse=False)
    mock_manager_instance.add_group.assert_any_call('group1')
    mock_manager_instance.add_group.assert_any_call('group2')
    mock_manager_instance.add_host.assert_any_call('host1', group='group1')
    mock_manager_instance.add_host.assert_any_call('host2', group='group1')
    mock_manager_instance.add_host.assert_any_call('host3', group='group2')
    mock_manager_instance.get_hosts.assert_called_once_with(pattern=terms)
    
    assert result == []
