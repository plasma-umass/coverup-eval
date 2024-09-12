# file: lib/ansible/plugins/inventory/constructed.py:128-135
# asked: {"lines": [128, 130, 132, 133, 135], "branches": [[132, 133], [132, 135]]}
# gained: {"lines": [128, 130, 132, 133, 135], "branches": [[132, 133], [132, 135]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.constructed import InventoryModule

@pytest.fixture
def mock_host():
    host = Mock()
    host.get_vars.return_value = {'initial': 'var'}
    return host

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_sources():
    return ['/some/path']

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.get_option = Mock(return_value=True)
    return module

@patch('ansible.plugins.inventory.constructed.combine_vars')
@patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources')
def test_host_vars_with_vars_plugins(mock_get_vars, mock_combine_vars, inventory_module, mock_host, mock_loader, mock_sources):
    mock_get_vars.return_value = {'plugin': 'var'}
    mock_combine_vars.return_value = {'combined': 'vars'}

    result = inventory_module.host_vars(mock_host, mock_loader, mock_sources)

    mock_host.get_vars.assert_called_once()
    mock_get_vars.assert_called_once_with(mock_loader, mock_sources, [mock_host], 'all')
    mock_combine_vars.assert_called_once_with({'initial': 'var'}, {'plugin': 'var'})
    assert result == {'combined': 'vars'}

@patch('ansible.plugins.inventory.constructed.combine_vars')
@patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources')
def test_host_vars_without_vars_plugins(mock_get_vars, mock_combine_vars, inventory_module, mock_host, mock_loader, mock_sources):
    inventory_module.get_option = Mock(return_value=False)

    result = inventory_module.host_vars(mock_host, mock_loader, mock_sources)

    mock_host.get_vars.assert_called_once()
    mock_get_vars.assert_not_called()
    mock_combine_vars.assert_not_called()
    assert result == {'initial': 'var'}
