# file: lib/ansible/inventory/data.py:236-243
# asked: {"lines": [236, 238, 239, 241, 242, 243], "branches": [[238, 239], [238, 241], [241, 0], [241, 242]]}
# gained: {"lines": [236, 238, 239, 241, 242, 243], "branches": [[238, 239], [241, 0], [241, 242]]}

import pytest
from unittest.mock import Mock

class TestInventoryData:
    
    @pytest.fixture
    def inventory_data(self):
        from ansible.inventory.data import InventoryData
        return InventoryData()

    def test_remove_host(self, inventory_data):
        # Create a mock host
        mock_host = Mock()
        mock_host.name = 'test_host'
        
        # Add the mock host to the inventory
        inventory_data.hosts[mock_host.name] = mock_host
        
        # Create a mock group and add it to the inventory
        mock_group = Mock()
        inventory_data.groups['test_group'] = mock_group
        
        # Call remove_host and verify the host is removed from hosts
        inventory_data.remove_host(mock_host)
        assert mock_host.name not in inventory_data.hosts
        
        # Verify remove_host is called on the group
        mock_group.remove_host.assert_called_once_with(mock_host)
