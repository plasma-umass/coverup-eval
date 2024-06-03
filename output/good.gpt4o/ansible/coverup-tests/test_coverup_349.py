# file lib/ansible/inventory/data.py:245-256
# lines [245, 248, 249, 250, 251, 253, 255, 256]
# branches ['248->249', '248->250', '250->251', '250->253']

import pytest
from unittest.mock import Mock, patch
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_set_variable_group(inventory_data, mocker):
    mock_group = Mock()
    inventory_data.groups = {'group1': mock_group}
    inventory_data.hosts = {}

    inventory_data.set_variable('group1', 'var1', 'value1')
    mock_group.set_variable.assert_called_once_with('var1', 'value1')

def test_set_variable_host(inventory_data, mocker):
    mock_host = Mock()
    inventory_data.groups = {}
    inventory_data.hosts = {'host1': mock_host}

    inventory_data.set_variable('host1', 'var1', 'value1')
    mock_host.set_variable.assert_called_once_with('var1', 'value1')

def test_set_variable_error(inventory_data):
    inventory_data.groups = {}
    inventory_data.hosts = {}

    with pytest.raises(AnsibleError, match="Could not identify group or host named unknown"):
        inventory_data.set_variable('unknown', 'var1', 'value1')
