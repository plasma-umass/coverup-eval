# file: lib/ansible/plugins/inventory/constructed.py:115-117
# asked: {"lines": [115, 117], "branches": []}
# gained: {"lines": [115, 117], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.constructed import InventoryModule

@pytest.fixture
def mock_host():
    return Mock()

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_sources():
    return Mock()

@pytest.fixture
def inventory_module():
    return InventoryModule()

@patch('ansible.plugins.inventory.constructed.InventoryModule.host_groupvars')
@patch('ansible.plugins.inventory.constructed.InventoryModule.host_vars')
@patch('ansible.plugins.inventory.constructed.combine_vars')
def test_get_all_host_vars(mock_combine_vars, mock_host_vars, mock_host_groupvars, inventory_module, mock_host, mock_loader, mock_sources):
    # Setup mock return values
    mock_host_groupvars.return_value = {'groupvar1': 'value1'}
    mock_host_vars.return_value = {'hostvar1': 'value2'}
    mock_combine_vars.return_value = {'groupvar1': 'value1', 'hostvar1': 'value2'}

    # Call the method
    result = inventory_module.get_all_host_vars(mock_host, mock_loader, mock_sources)

    # Assertions
    mock_host_groupvars.assert_called_once_with(mock_host, mock_loader, mock_sources)
    mock_host_vars.assert_called_once_with(mock_host, mock_loader, mock_sources)
    mock_combine_vars.assert_called_once_with({'groupvar1': 'value1'}, {'hostvar1': 'value2'})
    assert result == {'groupvar1': 'value1', 'hostvar1': 'value2'}
