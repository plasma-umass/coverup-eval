# file: lib/ansible/plugins/inventory/constructed.py:128-135
# asked: {"lines": [128, 130, 132, 133, 135], "branches": [[132, 133], [132, 135]]}
# gained: {"lines": [128, 130, 132, 133, 135], "branches": [[132, 133], [132, 135]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.constructed import InventoryModule

@pytest.fixture
def mock_host():
    host = Mock()
    host.get_vars.return_value = {'var1': 'value1'}
    return host

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_sources():
    return ['source1', 'source2']

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_host_vars_no_vars_plugins(inventory_module, mock_host, mock_loader, mock_sources, monkeypatch):
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: False)
    result = inventory_module.host_vars(mock_host, mock_loader, mock_sources)
    assert result == {'var1': 'value1'}

def test_host_vars_with_vars_plugins(inventory_module, mock_host, mock_loader, mock_sources, monkeypatch):
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: True)
    with patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources') as mock_get_vars:
        mock_get_vars.return_value = {'var2': 'value2'}
        with patch('ansible.plugins.inventory.constructed.combine_vars') as mock_combine_vars:
            mock_combine_vars.return_value = {'var1': 'value1', 'var2': 'value2'}
            result = inventory_module.host_vars(mock_host, mock_loader, mock_sources)
            assert result == {'var1': 'value1', 'var2': 'value2'}
            mock_get_vars.assert_called_once_with(mock_loader, mock_sources, [mock_host], 'all')
            mock_combine_vars.assert_called_once_with({'var1': 'value1'}, {'var2': 'value2'})
