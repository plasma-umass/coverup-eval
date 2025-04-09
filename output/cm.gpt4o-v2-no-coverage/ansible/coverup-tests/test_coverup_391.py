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

def test_set_variable_group(inventory_data, mocker):
    mocker.patch.object(inventory_data, 'groups', {'group1': MagicMock()})
    mocker.patch.object(inventory_data, 'hosts', {})
    mock_display = mocker.patch('ansible.inventory.data.display.debug')

    inventory_data.set_variable('group1', 'var1', 'value1')

    inventory_data.groups['group1'].set_variable.assert_called_once_with('var1', 'value1')
    mock_display.assert_called_once_with('set var1 for group1')

def test_set_variable_host(inventory_data, mocker):
    mocker.patch.object(inventory_data, 'groups', {})
    mocker.patch.object(inventory_data, 'hosts', {'host1': MagicMock()})
    mock_display = mocker.patch('ansible.inventory.data.display.debug')

    inventory_data.set_variable('host1', 'var1', 'value1')

    inventory_data.hosts['host1'].set_variable.assert_called_once_with('var1', 'value1')
    mock_display.assert_called_once_with('set var1 for host1')

def test_set_variable_error(inventory_data):
    with pytest.raises(AnsibleError, match="Could not identify group or host named unknown"):
        inventory_data.set_variable('unknown', 'var1', 'value1')
