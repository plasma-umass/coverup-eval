# file lib/ansible/plugins/inventory/constructed.py:137-177
# lines [140, 142, 144, 145, 146, 147, 148, 149, 151, 152, 153, 155, 158, 159, 160, 163, 166, 167, 168, 171, 174, 176, 177]
# branches ['148->149', '148->151', '155->exit', '155->158', '159->160', '159->163', '167->168', '167->171']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.errors import AnsibleOptionsError, AnsibleParserError
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_inventory():
    inventory = MagicMock(spec=InventoryManager)
    inventory.hosts = {
        'host1': MagicMock(),
        'host2': MagicMock()
    }
    inventory.processed_sources = ['source1']
    return inventory

@pytest.fixture
def mock_loader():
    return MagicMock(spec=DataLoader)

@pytest.fixture
def mock_path():
    return 'dummy_path'

@pytest.fixture
def mock_fact_cache():
    with patch('ansible.plugins.inventory.constructed.FactCache', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_get_option():
    with patch.object(InventoryModule, 'get_option', autospec=True) as mock:
        mock.side_effect = lambda self, option: {
            'use_vars_plugins': False,
            'strict': True,
            'compose': {},
            'groups': {},
            'keyed_groups': {}
        }[option]
        yield mock

@pytest.fixture
def mock_get_all_host_vars():
    with patch.object(InventoryModule, 'get_all_host_vars', autospec=True) as mock:
        mock.return_value = {}
        yield mock

@pytest.fixture
def mock_set_composite_vars():
    with patch.object(InventoryModule, '_set_composite_vars', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_add_host_to_composed_groups():
    with patch.object(InventoryModule, '_add_host_to_composed_groups', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_add_host_to_keyed_groups():
    with patch.object(InventoryModule, '_add_host_to_keyed_groups', autospec=True) as mock:
        yield mock

def test_parse(mock_inventory, mock_loader, mock_path, mock_fact_cache, mock_get_option, mock_get_all_host_vars, mock_set_composite_vars, mock_add_host_to_composed_groups, mock_add_host_to_keyed_groups):
    inventory_module = InventoryModule()
    
    # Mocking the _read_config_data method
    with patch.object(inventory_module, '_read_config_data', autospec=True) as mock_read_config_data:
        inventory_module.parse(mock_inventory, mock_loader, mock_path, cache=False)
        
        mock_read_config_data.assert_called_once_with(mock_path)
        mock_get_option.assert_any_call(inventory_module, 'strict')
        mock_get_option.assert_any_call(inventory_module, 'compose')
        mock_get_option.assert_any_call(inventory_module, 'groups')
        mock_get_option.assert_any_call(inventory_module, 'keyed_groups')
        
        for host in mock_inventory.hosts:
            mock_get_all_host_vars.assert_any_call(inventory_module, mock_inventory.hosts[host], mock_loader, ['source1'])
            mock_set_composite_vars.assert_any_call(inventory_module, {}, {}, host, strict=True)
            mock_add_host_to_composed_groups.assert_any_call(inventory_module, {}, {}, host, strict=True, fetch_hostvars=False)
            mock_add_host_to_keyed_groups.assert_any_call(inventory_module, {}, {}, host, strict=True, fetch_hostvars=False)
