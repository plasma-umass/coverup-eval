# file: lib/ansible/inventory/manager.py:181-182
# asked: {"lines": [182], "branches": []}
# gained: {"lines": [182], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

def test_add_host_to_inventory(mocker):
    loader = mocker.Mock()
    inventory_manager = InventoryManager(loader)
    
    # Mock the InventoryData's add_host method
    mock_add_host = mocker.patch.object(InventoryData, 'add_host', return_value='test_host')
    
    host = 'test_host'
    group = 'test_group'
    port = 1234
    
    # Call the add_host method
    result = inventory_manager.add_host(host, group, port)
    
    # Assert that the add_host method of InventoryData was called with the correct parameters
    mock_add_host.assert_called_once_with(host, group, port)
    
    # Assert the result
    assert result == 'test_host'

def test_add_host_invalid_host(mocker):
    loader = mocker.Mock()
    inventory_manager = InventoryManager(loader)
    
    # Mock the InventoryData's add_host method to raise an AnsibleError
    mocker.patch.object(InventoryData, 'add_host', side_effect=AnsibleError('Invalid host name supplied'))
    
    host = None
    group = 'test_group'
    port = 1234
    
    # Call the add_host method and assert that it raises an AnsibleError
    with pytest.raises(AnsibleError, match='Invalid host name supplied'):
        inventory_manager.add_host(host, group, port)
