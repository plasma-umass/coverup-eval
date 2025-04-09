# file: lib/ansible/plugins/inventory/constructed.py:115-117
# asked: {"lines": [115, 117], "branches": []}
# gained: {"lines": [115, 117], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.constructed import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def mock_host():
    host = Mock()
    host.get_groups.return_value = ['group1', 'group2']
    host.get_vars.return_value = {'var1': 'value1'}
    return host

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_sources():
    return ['source1', 'source2']

@patch('ansible.plugins.inventory.constructed.get_group_vars')
@patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources')
@patch('ansible.plugins.inventory.constructed.combine_vars')
def test_get_all_host_vars(mock_combine_vars, mock_get_vars_from_inventory_sources, mock_get_group_vars, inventory_module, mock_host, mock_loader, mock_sources):
    mock_get_group_vars.return_value = {'group_var1': 'group_value1'}
    mock_get_vars_from_inventory_sources.return_value = {'plugin_var1': 'plugin_value1'}
    mock_combine_vars.side_effect = lambda x, y: {**x, **y}

    inventory_module.get_option = Mock(return_value=True)

    result = inventory_module.get_all_host_vars(mock_host, mock_loader, mock_sources)

    mock_get_group_vars.assert_called_once_with(mock_host.get_groups())
    mock_get_vars_from_inventory_sources.assert_any_call(mock_loader, mock_sources, mock_host.get_groups(), 'all')
    mock_get_vars_from_inventory_sources.assert_any_call(mock_loader, mock_sources, [mock_host], 'all')
    mock_combine_vars.assert_any_call({'group_var1': 'group_value1'}, {'plugin_var1': 'plugin_value1'})
    mock_combine_vars.assert_any_call({'var1': 'value1'}, {'plugin_var1': 'plugin_value1'})

    assert result == {
        'group_var1': 'group_value1',
        'plugin_var1': 'plugin_value1',
        'var1': 'value1'
    }
