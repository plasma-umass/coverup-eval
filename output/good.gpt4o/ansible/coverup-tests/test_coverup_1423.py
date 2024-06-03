# file lib/ansible/inventory/manager.py:590-599
# lines [593, 596, 597, 599]
# branches ['596->597', '596->599']

import pytest
from unittest import mock
from ansible.inventory.manager import InventoryManager
import ansible.constants as C

@pytest.fixture
def inventory_manager(mocker):
    # Mock the loader argument required by InventoryManager
    mock_loader = mocker.Mock()
    return InventoryManager(loader=mock_loader)

def test_list_hosts_with_empty_result_and_localhost_pattern(inventory_manager, mocker):
    # Mock the get_hosts method to return an empty list
    mocker.patch.object(inventory_manager, 'get_hosts', return_value=[])
    
    # Mock the LOCALHOST constant to include the pattern
    mocker.patch.object(C, 'LOCALHOST', ['localhost'])
    
    pattern = 'localhost'
    result = inventory_manager.list_hosts(pattern)
    
    # Assert that the result is the pattern itself when get_hosts returns an empty list
    assert result == [pattern]
