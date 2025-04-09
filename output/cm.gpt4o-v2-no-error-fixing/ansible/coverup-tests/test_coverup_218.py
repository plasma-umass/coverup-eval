# file: lib/ansible/inventory/data.py:245-256
# asked: {"lines": [245, 248, 249, 250, 251, 253, 255, 256], "branches": [[248, 249], [248, 250], [250, 251], [250, 253]]}
# gained: {"lines": [245, 248, 249, 250, 251, 253, 255, 256], "branches": [[248, 249], [248, 250], [250, 251], [250, 253]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from unittest.mock import MagicMock, patch

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_set_variable_group(inventory_data):
    inventory_data.groups = {'group1': MagicMock()}
    inventory_data.hosts = {}
    inventory_data.groups['group1'].set_variable = MagicMock()

    inventory_data.set_variable('group1', 'var1', 'value1')

    inventory_data.groups['group1'].set_variable.assert_called_once_with('var1', 'value1')

def test_set_variable_host(inventory_data):
    inventory_data.groups = {}
    inventory_data.hosts = {'host1': MagicMock()}
    inventory_data.hosts['host1'].set_variable = MagicMock()

    inventory_data.set_variable('host1', 'var1', 'value1')

    inventory_data.hosts['host1'].set_variable.assert_called_once_with('var1', 'value1')

def test_set_variable_entity_not_found(inventory_data):
    inventory_data.groups = {}
    inventory_data.hosts = {}

    with pytest.raises(AnsibleError, match="Could not identify group or host named entity1"):
        inventory_data.set_variable('entity1', 'var1', 'value1')

@patch('ansible.inventory.data.display')
def test_set_variable_debug(mock_display, inventory_data):
    inventory_data.groups = {'group1': MagicMock()}
    inventory_data.hosts = {}
    inventory_data.groups['group1'].set_variable = MagicMock()

    inventory_data.set_variable('group1', 'var1', 'value1')

    mock_display.debug.assert_called_once_with('set var1 for group1')
