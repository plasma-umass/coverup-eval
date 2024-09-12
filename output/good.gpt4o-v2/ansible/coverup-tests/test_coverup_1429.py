# file: lib/ansible/plugins/inventory/advanced_host_list.py:31-63
# asked: {"lines": [], "branches": [[60, 59]]}
# gained: {"lines": [], "branches": [[60, 59]]}

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory.advanced_host_list import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin

class MockInventory:
    def __init__(self):
        self.hosts = {}

    def add_host(self, host, group, port):
        self.hosts[host] = {'group': group, 'port': port}

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def mock_inventory():
    return MockInventory()

def test_parse_with_new_host(mocker, inventory_module, mock_inventory):
    mocker.patch.object(inventory_module, 'inventory', mock_inventory)
    mocker.patch.object(inventory_module, '_expand_hostpattern', return_value=(['new_host'], None))
    mocker.patch.object(inventory_module, 'display', mocker.Mock())

    inventory_module.parse(mock_inventory, None, 'new_host')

    assert 'new_host' in mock_inventory.hosts
    assert mock_inventory.hosts['new_host']['group'] == 'ungrouped'
    assert mock_inventory.hosts['new_host']['port'] is None

def test_parse_with_existing_host(mocker, inventory_module, mock_inventory):
    mock_inventory.add_host('existing_host', 'ungrouped', None)
    mocker.patch.object(inventory_module, 'inventory', mock_inventory)
    mocker.patch.object(inventory_module, '_expand_hostpattern', return_value=(['existing_host'], None))
    mocker.patch.object(inventory_module, 'display', mocker.Mock())

    inventory_module.parse(mock_inventory, None, 'existing_host')

    assert 'existing_host' in mock_inventory.hosts
    assert mock_inventory.hosts['existing_host']['group'] == 'ungrouped'
    assert mock_inventory.hosts['existing_host']['port'] is None

def test_parse_with_invalid_host(mocker, inventory_module, mock_inventory):
    mocker.patch.object(inventory_module, 'inventory', mock_inventory)
    mocker.patch.object(inventory_module, '_expand_hostpattern', side_effect=AnsibleError('error'))
    mocker.patch.object(inventory_module, 'display', mocker.Mock())

    inventory_module.parse(mock_inventory, None, 'invalid_host')

    assert 'invalid_host' in mock_inventory.hosts
    assert mock_inventory.hosts['invalid_host']['group'] == 'ungrouped'
    assert mock_inventory.hosts['invalid_host']['port'] is None

def test_parse_with_exception(mocker, inventory_module, mock_inventory):
    mocker.patch.object(inventory_module, 'inventory', mock_inventory)
    mocker.patch.object(inventory_module, '_expand_hostpattern', side_effect=Exception('error'))
    mocker.patch.object(inventory_module, 'display', mocker.Mock())

    with pytest.raises(AnsibleParserError, match='Invalid data from string, could not parse: error'):
        inventory_module.parse(mock_inventory, None, 'exception_host')
