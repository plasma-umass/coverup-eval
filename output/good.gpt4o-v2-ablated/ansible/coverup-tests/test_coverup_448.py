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

def test_host_groupvars_no_vars_plugins(inventory_module, mock_host, mock_loader, mock_sources, monkeypatch):
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: False)
    with patch('ansible.plugins.inventory.constructed.get_group_vars', return_value={'var1': 'value1'}) as mock_get_group_vars:
        gvars = inventory_module.host_groupvars(mock_host, mock_loader, mock_sources)
        mock_get_group_vars.assert_called_once_with(mock_host.get_groups())
        assert gvars == {'var1': 'value1'}

def test_host_groupvars_with_vars_plugins(inventory_module, mock_host, mock_loader, mock_sources, monkeypatch):
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: True)
    with patch('ansible.plugins.inventory.constructed.get_group_vars', return_value={'var1': 'value1'}) as mock_get_group_vars, \
         patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources', return_value={'var2': 'value2'}) as mock_get_vars_from_inventory_sources, \
         patch('ansible.plugins.inventory.constructed.combine_vars', return_value={'var1': 'value1', 'var2': 'value2'}) as mock_combine_vars:
        gvars = inventory_module.host_groupvars(mock_host, mock_loader, mock_sources)
        mock_get_group_vars.assert_called_once_with(mock_host.get_groups())
        mock_get_vars_from_inventory_sources.assert_called_once_with(mock_loader, mock_sources, mock_host.get_groups(), 'all')
        mock_combine_vars.assert_called_once_with({'var1': 'value1'}, {'var2': 'value2'})
        assert gvars == {'var1': 'value1', 'var2': 'value2'}
