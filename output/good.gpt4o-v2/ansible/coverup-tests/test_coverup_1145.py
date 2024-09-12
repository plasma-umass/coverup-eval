# file: lib/ansible/cli/inventory.py:266-282
# asked: {"lines": [268, 269, 270, 271, 273, 274, 275, 276, 277, 279, 280, 282], "branches": [[270, 271], [270, 273], [273, 274], [273, 279], [274, 275], [274, 279], [276, 274], [276, 277], [279, 280], [279, 282]]}
# gained: {"lines": [268, 269, 270, 271, 273, 274, 275, 276, 277, 279, 280, 282], "branches": [[270, 271], [270, 273], [273, 274], [274, 275], [274, 279], [276, 277], [279, 280], [279, 282]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def mock_group():
    group = MagicMock()
    group.name = 'test_group'
    group.child_groups = []
    group.hosts = []
    return group

@pytest.fixture
def mock_host():
    host = MagicMock()
    host.name = 'test_host'
    return host

@pytest.fixture
def inventory_cli():
    return InventoryCLI(args=['test_arg'])

def test_graph_group_with_child_groups(inventory_cli, mock_group):
    child_group = MagicMock()
    child_group.name = 'child_group'
    child_group.child_groups = []
    child_group.hosts = []
    mock_group.child_groups = [child_group]

    with patch('ansible.cli.inventory.InventoryCLI._graph_name', return_value='graph_name'), \
         patch('ansible.cli.inventory.InventoryCLI._show_vars', return_value=['var1', 'var2']), \
         patch('ansible.cli.inventory.InventoryCLI._get_host_variables', return_value={'var': 'value'}), \
         patch('ansible.cli.inventory.InventoryCLI._get_group_variables', return_value={'var': 'value'}), \
         patch('ansible.context.CLIARGS', {'show_vars': True}):
        
        result = inventory_cli._graph_group(mock_group)
        assert 'graph_name' in result
        assert 'var1' in result
        assert 'var2' in result

def test_graph_group_with_hosts(inventory_cli, mock_group, mock_host):
    mock_group.hosts = [mock_host]

    with patch('ansible.cli.inventory.InventoryCLI._graph_name', return_value='graph_name'), \
         patch('ansible.cli.inventory.InventoryCLI._show_vars', return_value=['var1', 'var2']), \
         patch('ansible.cli.inventory.InventoryCLI._get_host_variables', return_value={'var': 'value'}), \
         patch('ansible.cli.inventory.InventoryCLI._get_group_variables', return_value={'var': 'value'}), \
         patch('ansible.context.CLIARGS', {'show_vars': True}):
        
        result = inventory_cli._graph_group(mock_group)
        assert 'graph_name' in result
        assert 'var1' in result
        assert 'var2' in result

def test_graph_group_with_show_vars(inventory_cli, mock_group):
    with patch('ansible.cli.inventory.InventoryCLI._graph_name', return_value='graph_name'), \
         patch('ansible.cli.inventory.InventoryCLI._show_vars', return_value=['var1', 'var2']), \
         patch('ansible.cli.inventory.InventoryCLI._get_host_variables', return_value={'var': 'value'}), \
         patch('ansible.cli.inventory.InventoryCLI._get_group_variables', return_value={'var': 'value'}), \
         patch('ansible.context.CLIARGS', {'show_vars': True}):
        
        result = inventory_cli._graph_group(mock_group)
        assert 'graph_name' in result
        assert 'var1' in result
        assert 'var2' in result

def test_graph_group_without_show_vars(inventory_cli, mock_group):
    with patch('ansible.cli.inventory.InventoryCLI._graph_name', return_value='graph_name'), \
         patch('ansible.cli.inventory.InventoryCLI._show_vars', return_value=['var1', 'var2']), \
         patch('ansible.cli.inventory.InventoryCLI._get_host_variables', return_value={'var': 'value'}), \
         patch('ansible.cli.inventory.InventoryCLI._get_group_variables', return_value={'var': 'value'}), \
         patch('ansible.context.CLIARGS', {'show_vars': False}):
        
        result = inventory_cli._graph_group(mock_group)
        assert 'graph_name' in result
        assert 'var1' not in result
        assert 'var2' not in result
