# file: lib/ansible/plugins/inventory/constructed.py:119-126
# asked: {"lines": [121, 123, 124, 126], "branches": [[123, 124], [123, 126]]}
# gained: {"lines": [121, 123, 124, 126], "branches": [[123, 124], [123, 126]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.inventory.constructed import InventoryModule

@pytest.fixture
def mock_host():
    host = MagicMock()
    host.get_groups.return_value = ['group1', 'group2']
    return host

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_sources():
    return ['source1', 'source2']

@pytest.fixture
def inventory_module():
    return InventoryModule()

@patch('ansible.plugins.inventory.constructed.get_group_vars')
@patch('ansible.plugins.inventory.constructed.combine_vars')
@patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources')
def test_host_groupvars_use_vars_plugins_enabled(mock_get_vars_from_inventory_sources, mock_combine_vars, mock_get_group_vars, inventory_module, mock_host, mock_loader, mock_sources, monkeypatch):
    # Mock the return values
    mock_get_group_vars.return_value = {'var1': 'value1'}
    mock_get_vars_from_inventory_sources.return_value = {'var2': 'value2'}
    mock_combine_vars.return_value = {'var1': 'value1', 'var2': 'value2'}
    
    # Mock the get_option method to return True for 'use_vars_plugins'
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: True if x == 'use_vars_plugins' else None)
    
    # Call the method
    result = inventory_module.host_groupvars(mock_host, mock_loader, mock_sources)
    
    # Assertions
    mock_get_group_vars.assert_called_once_with(mock_host.get_groups())
    mock_get_vars_from_inventory_sources.assert_called_once_with(mock_loader, mock_sources, mock_host.get_groups(), 'all')
    mock_combine_vars.assert_called_once_with({'var1': 'value1'}, {'var2': 'value2'})
    assert result == {'var1': 'value1', 'var2': 'value2'}

@patch('ansible.plugins.inventory.constructed.get_group_vars')
def test_host_groupvars_use_vars_plugins_disabled(mock_get_group_vars, inventory_module, mock_host, mock_loader, mock_sources, monkeypatch):
    # Mock the return values
    mock_get_group_vars.return_value = {'var1': 'value1'}
    
    # Mock the get_option method to return False for 'use_vars_plugins'
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: False if x == 'use_vars_plugins' else None)
    
    # Call the method
    result = inventory_module.host_groupvars(mock_host, mock_loader, mock_sources)
    
    # Assertions
    mock_get_group_vars.assert_called_once_with(mock_host.get_groups())
    assert result == {'var1': 'value1'}
