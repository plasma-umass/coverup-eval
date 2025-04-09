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

def test_host_vars_without_vars_plugins(mock_host, mock_loader, mock_sources, inventory_module):
    with patch.object(inventory_module, 'get_option', return_value=False):
        hvars = inventory_module.host_vars(mock_host, mock_loader, mock_sources)
        assert hvars == {'var1': 'value1'}

def test_host_vars_with_vars_plugins(mock_host, mock_loader, mock_sources, inventory_module):
    with patch.object(inventory_module, 'get_option', return_value=True), \
         patch('ansible.plugins.inventory.constructed.combine_vars', return_value={'var1': 'value1', 'var2': 'value2'}), \
         patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources', return_value={'var2': 'value2'}):
        hvars = inventory_module.host_vars(mock_host, mock_loader, mock_sources)
        assert hvars == {'var1': 'value1', 'var2': 'value2'}
