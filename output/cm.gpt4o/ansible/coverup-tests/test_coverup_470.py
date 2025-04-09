# file lib/ansible/inventory/data.py:275-283
# lines [275, 279, 280, 281, 283]
# branches ['279->280', '279->283', '280->281', '280->283']

import pytest
from unittest.mock import MagicMock

# Assuming the InventoryData class is imported from ansible.inventory.data
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_data():
    inventory = InventoryData()
    inventory._groups_dict_cache = {}
    inventory.groups = {
        'group1': MagicMock(get_hosts=MagicMock(return_value=[MagicMock(name='host1'), MagicMock(name='host2')])),
        'group2': MagicMock(get_hosts=MagicMock(return_value=[MagicMock(name='host3')])),
    }
    inventory.groups['group1'].get_hosts.return_value[0].name = 'host1'
    inventory.groups['group1'].get_hosts.return_value[1].name = 'host2'
    inventory.groups['group2'].get_hosts.return_value[0].name = 'host3'
    return inventory

def test_get_groups_dict(inventory_data):
    result = inventory_data.get_groups_dict()
    
    assert 'group1' in result
    assert 'group2' in result
    assert result['group1'] == ['host1', 'host2']
    assert result['group2'] == ['host3']

    # Ensure cache is used on subsequent calls
    inventory_data.groups['group1'].get_hosts.assert_called_once()
    inventory_data.groups['group2'].get_hosts.assert_called_once()
    
    result_cached = inventory_data.get_groups_dict()
    assert result == result_cached
