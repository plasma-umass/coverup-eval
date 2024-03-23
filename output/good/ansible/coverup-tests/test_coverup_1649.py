# file lib/ansible/plugins/inventory/constructed.py:128-135
# lines [130, 132, 133, 135]
# branches ['132->133', '132->135']

import pytest
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.inventory.host import Host
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.utils.vars import combine_vars

# Mock classes and functions
class MockLoader(DataLoader):
    pass

class MockSources(list):
    pass

def mock_get_vars_from_inventory_sources(loader, sources, hosts, group_name):
    return {'mocked_var': 'mocked_value'}

# Test function
def test_host_vars_with_use_vars_plugins(mocker):
    # Setup
    mocker.patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources', side_effect=mock_get_vars_from_inventory_sources)
    mocker.patch('ansible.plugins.inventory.constructed.C.config.get_plugin_options', return_value={'use_vars_plugins': True})
    inventory_module = InventoryModule()
    inventory_module._load_name = 'constructed'  # Mocking the load name
    inventory_module.set_options()
    host = Host(name='testhost')
    host.vars = {'original_var': 'original_value'}
    loader = MockLoader()
    sources = MockSources()

    # Act
    result_vars = inventory_module.host_vars(host, loader, sources)

    # Assert
    assert 'original_var' in result_vars
    assert result_vars['original_var'] == 'original_value'
    assert 'mocked_var' in result_vars
    assert result_vars['mocked_var'] == 'mocked_value'

    # Cleanup is handled by pytest fixtures automatically
