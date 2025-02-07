# file: lib/ansible/plugins/lookup/inventory_hostnames.py:42-53
# asked: {"lines": [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53], "branches": [[45, 46], [45, 50], [47, 45], [47, 48]]}
# gained: {"lines": [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53], "branches": [[45, 46], [45, 50], [47, 45], [47, 48]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.plugins.lookup.inventory_hostnames import LookupModule

@pytest.fixture
def mock_inventory_manager(mocker):
    mocker.patch('ansible.inventory.manager.InventoryManager.add_group')
    mocker.patch('ansible.inventory.manager.InventoryManager.add_host')
    mocker.patch('ansible.inventory.manager.InventoryManager.get_hosts', return_value=[])

def test_lookup_module_run_success(mock_inventory_manager):
    lookup = LookupModule()
    terms = 'all'
    variables = {
        'groups': {
            'group1': ['host1', 'host2'],
            'group2': ['host3']
        }
    }
    result = lookup.run(terms, variables)
    assert result == []

def test_lookup_module_run_ansible_error(mock_inventory_manager, mocker):
    mocker.patch('ansible.inventory.manager.InventoryManager.get_hosts', side_effect=AnsibleError)
    lookup = LookupModule()
    terms = 'all'
    variables = {
        'groups': {
            'group1': ['host1', 'host2'],
            'group2': ['host3']
        }
    }
    result = lookup.run(terms, variables)
    assert result == []
