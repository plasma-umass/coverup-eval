# file lib/ansible/plugins/inventory/constructed.py:119-126
# lines [121, 123, 124, 126]
# branches ['123->124', '123->126']

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.constructed import InventoryModule

@pytest.fixture
def mock_host():
    host = Mock()
    host.get_groups.return_value = ['group1', 'group2']
    return host

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_sources():
    return ['source1', 'source2']

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.get_option = Mock(return_value=True)
    return module

@patch('ansible.plugins.inventory.constructed.get_group_vars')
@patch('ansible.plugins.inventory.constructed.combine_vars')
@patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources')
def test_host_groupvars(mock_get_vars_from_inventory_sources, mock_combine_vars, mock_get_group_vars, inventory_module, mock_host, mock_loader, mock_sources):
    mock_get_group_vars.return_value = {'var1': 'value1'}
    mock_get_vars_from_inventory_sources.return_value = {'var2': 'value2'}
    mock_combine_vars.return_value = {'var1': 'value1', 'var2': 'value2'}

    gvars = inventory_module.host_groupvars(mock_host, mock_loader, mock_sources)

    mock_get_group_vars.assert_called_once_with(mock_host.get_groups())
    mock_get_vars_from_inventory_sources.assert_called_once_with(mock_loader, mock_sources, mock_host.get_groups(), 'all')
    mock_combine_vars.assert_called_once_with({'var1': 'value1'}, {'var2': 'value2'})
    assert gvars == {'var1': 'value1', 'var2': 'value2'}
