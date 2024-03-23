# file lib/ansible/inventory/data.py:42-59
# lines [42, 44, 45, 48, 51, 53, 54, 57, 58, 59]
# branches ['57->58', '57->59']

import pytest
from ansible.inventory.data import InventoryData

class TestInventoryData:

    def test_inventory_data_initialization(self, mocker):
        # Setup
        mocker.patch.object(InventoryData, 'add_group')
        mocker.patch.object(InventoryData, 'add_child')

        # Exercise
        inventory_data = InventoryData()

        # Verify
        assert inventory_data.groups == {}
        assert inventory_data.hosts == {}
        assert inventory_data._groups_dict_cache == {}
        assert inventory_data.localhost is None
        assert inventory_data.current_source is None
        assert inventory_data.processed_sources == []
        inventory_data.add_group.assert_has_calls([mocker.call('all'), mocker.call('ungrouped')])
        inventory_data.add_child.assert_called_once_with('all', 'ungrouped')

        # Cleanup - nothing to clean up as we are using mocks
