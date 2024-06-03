# file lib/ansible/plugins/inventory/constructed.py:115-117
# lines [115, 117]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.constructed import InventoryModule

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_sources():
    return Mock()

@pytest.fixture
def mock_host():
    return Mock()

@pytest.fixture
def inventory_module():
    return InventoryModule()

@patch('ansible.plugins.inventory.constructed.combine_vars')
@patch('ansible.plugins.inventory.constructed.InventoryModule.host_groupvars')
@patch('ansible.plugins.inventory.constructed.InventoryModule.host_vars')
def test_get_all_host_vars(mock_host_vars, mock_host_groupvars, mock_combine_vars, inventory_module, mock_host, mock_loader, mock_sources):
    # Setup mock return values
    mock_host_groupvars.return_value = {'group_var1': 'value1'}
    mock_host_vars.return_value = {'host_var1': 'value2'}
    mock_combine_vars.return_value = {'group_var1': 'value1', 'host_var1': 'value2'}

    # Call the method
    result = inventory_module.get_all_host_vars(mock_host, mock_loader, mock_sources)

    # Assertions
    mock_host_groupvars.assert_called_once_with(mock_host, mock_loader, mock_sources)
    mock_host_vars.assert_called_once_with(mock_host, mock_loader, mock_sources)
    mock_combine_vars.assert_called_once_with({'group_var1': 'value1'}, {'host_var1': 'value2'})
    assert result == {'group_var1': 'value1', 'host_var1': 'value2'}
