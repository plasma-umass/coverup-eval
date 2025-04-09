# file lib/ansible/plugins/inventory/constructed.py:119-126
# lines []
# branches ['123->126']

import pytest
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.parsing.dataloader import DataLoader

# Mock functions to be used in the test
def mock_get_group_vars(groups):
    return {'some_group_var': 'value'}

def mock_get_vars_from_inventory_sources(loader, sources, groups, scope):
    return {'some_other_var': 'another_value'}

# Test function to cover the missing branch
@pytest.fixture
def inventory_module(mocker):
    mocker.patch('ansible.plugins.inventory.constructed.get_group_vars', side_effect=mock_get_group_vars)
    mocker.patch('ansible.plugins.inventory.constructed.get_vars_from_inventory_sources', side_effect=mock_get_vars_from_inventory_sources)
    inventory_module = InventoryModule()
    # Mock the _load_name attribute which is required by set_options
    inventory_module._load_name = 'constructed'
    # Mock the get_option method to return True for 'use_vars_plugins'
    mocker.patch.object(inventory_module, 'get_option', return_value=True)
    return inventory_module

def test_host_groupvars_with_use_vars_plugins(inventory_module):
    # Setup host and groups
    host = Host(name='testhost')
    group = Group(name='testgroup')
    host.add_group(group)

    # Mock loader and sources
    loader = DataLoader()
    sources = []

    # Call the function under test
    gvars = inventory_module.host_groupvars(host, loader, sources)

    # Assertions to verify postconditions
    assert 'some_group_var' in gvars
    assert 'some_other_var' in gvars
    assert gvars['some_group_var'] == 'value'
    assert gvars['some_other_var'] == 'another_value'

# Test function to cover the missing branch when 'use_vars_plugins' is False
def test_host_groupvars_without_use_vars_plugins(inventory_module, mocker):
    # Override the get_option mock to return False for 'use_vars_plugins'
    mocker.patch.object(inventory_module, 'get_option', return_value=False)

    # Setup host and groups
    host = Host(name='testhost')
    group = Group(name='testgroup')
    host.add_group(group)

    # Mock loader and sources
    loader = DataLoader()
    sources = []

    # Call the function under test
    gvars = inventory_module.host_groupvars(host, loader, sources)

    # Assertions to verify postconditions
    assert 'some_group_var' in gvars
    # 'some_other_var' should not be in gvars because 'use_vars_plugins' is False
    assert 'some_other_var' not in gvars
    assert gvars['some_group_var'] == 'value'
