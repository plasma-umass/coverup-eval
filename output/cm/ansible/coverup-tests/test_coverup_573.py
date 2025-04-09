# file lib/ansible/plugins/inventory/constructed.py:119-126
# lines [119, 121, 123, 124, 126]
# branches ['123->124', '123->126']

import pytest
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.parsing.dataloader import DataLoader
from ansible.utils.vars import combine_vars

# Mock functions to be used in the test
def mock_get_group_vars(groups):
    return {'group_var': 'group_value'}

def mock_get_vars_from_inventory_sources(loader, sources, groups, scope):
    return {'vars_plugin_var': 'vars_plugin_value'}

# Test function
def test_host_groupvars(mocker):
    # Mock the necessary functions
    mocker.patch('ansible.plugins.inventory.constructed.get_group_vars', side_effect=mock_get_group_vars)
    mocker.patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources', side_effect=mock_get_vars_from_inventory_sources)
    mocker.patch('ansible.plugins.inventory.constructed.combine_vars', side_effect=combine_vars)

    # Create necessary objects
    inventory_module = InventoryModule()
    inventory_module._options = {'use_vars_plugins': True}
    host = Host(name='test_host')
    group = Group(name='test_group')
    host.add_group(group)
    loader = DataLoader()
    sources = ''

    # Call the method under test
    gvars = inventory_module.host_groupvars(host, loader, sources)

    # Assertions to verify postconditions
    assert 'group_var' in gvars
    assert gvars['group_var'] == 'group_value'
    assert 'vars_plugin_var' in gvars
    assert gvars['vars_plugin_var'] == 'vars_plugin_value'
