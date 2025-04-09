# file: lib/ansible/cli/inventory.py:328-363
# asked: {"lines": [330, 332, 333, 336, 339, 340, 341, 342, 345, 346, 347, 348, 349, 350, 351, 352, 354, 355, 356, 357, 359, 361, 363], "branches": [[340, 341], [340, 345], [341, 340], [341, 342], [346, 347], [346, 354], [347, 348], [347, 354], [349, 350], [349, 352], [354, 355], [354, 359], [356, 357], [356, 359]]}
# gained: {"lines": [330, 332, 333, 336, 339, 340, 341, 342, 345, 346, 347, 348, 349, 350, 351, 352, 354, 355, 356, 357, 359, 361, 363], "branches": [[340, 341], [340, 345], [341, 342], [346, 347], [347, 348], [347, 354], [349, 350], [354, 355], [354, 359], [356, 357]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.inventory import InventoryCLI
from ansible import context

@pytest.fixture
def mock_group():
    group = MagicMock()
    group.name = 'group1'
    group.child_groups = []
    group.hosts = []
    return group

@pytest.fixture
def mock_host():
    host = MagicMock()
    host.name = 'host1'
    return host

@pytest.fixture
def inventory_cli():
    cli = InventoryCLI(args=['dummy_arg'])
    cli._get_host_variables = MagicMock(return_value={'var1': 'value1'})
    cli._get_group_variables = MagicMock(return_value={'gvar1': 'gvalue1'})
    cli._remove_empty = MagicMock()
    return cli

def test_yaml_inventory_no_children_no_hosts(inventory_cli, mock_group):
    context.CLIARGS = {'export': False}
    result = inventory_cli.yaml_inventory(mock_group)
    assert result == {'group1': {'children': {}, 'hosts': {}}}
    inventory_cli._remove_empty.assert_called_once_with({'children': {}, 'hosts': {}})

def test_yaml_inventory_with_children(inventory_cli, mock_group):
    subgroup = MagicMock()
    subgroup.name = 'subgroup1'
    subgroup.child_groups = []
    subgroup.hosts = []
    mock_group.child_groups = [subgroup]
    
    context.CLIARGS = {'export': False}
    result = inventory_cli.yaml_inventory(mock_group)
    assert result == {'group1': {'children': {'subgroup1': {'children': {}, 'hosts': {}}}, 'hosts': {}}}
    inventory_cli._remove_empty.assert_called_with({'children': {'subgroup1': {'children': {}, 'hosts': {}}}, 'hosts': {}})

def test_yaml_inventory_with_hosts(inventory_cli, mock_group, mock_host):
    mock_group.hosts = [mock_host]
    
    context.CLIARGS = {'export': False}
    result = inventory_cli.yaml_inventory(mock_group)
    assert result == {'group1': {'children': {}, 'hosts': {'host1': {'var1': 'value1'}}}}
    inventory_cli._remove_empty.assert_called_once_with({'children': {}, 'hosts': {'host1': {'var1': 'value1'}}})

def test_yaml_inventory_with_export(inventory_cli, mock_group):
    context.CLIARGS = {'export': True}
    result = inventory_cli.yaml_inventory(mock_group)
    assert result == {'group1': {'children': {}, 'hosts': {}, 'vars': {'gvar1': 'gvalue1'}}}
    inventory_cli._remove_empty.assert_called_once_with({'children': {}, 'hosts': {}, 'vars': {'gvar1': 'gvalue1'}})
