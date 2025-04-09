# file: lib/ansible/cli/inventory.py:266-282
# asked: {"lines": [266, 268, 269, 270, 271, 273, 274, 275, 276, 277, 279, 280, 282], "branches": [[270, 271], [270, 273], [273, 274], [273, 279], [274, 275], [274, 279], [276, 274], [276, 277], [279, 280], [279, 282]]}
# gained: {"lines": [266, 268, 269, 270, 271, 273, 274, 275, 276, 277, 279, 280, 282], "branches": [[270, 271], [270, 273], [273, 274], [274, 275], [274, 279], [276, 274], [276, 277], [279, 280], [279, 282]]}

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
def mock_context():
    with patch('ansible.context.CLIARGS', {'show_vars': False, 'export': False, 'basedir': None}):
        yield

@pytest.fixture
def inventory_cli():
    args = MagicMock()
    return InventoryCLI(args)

def test_graph_group_no_children_no_hosts(mock_group, mock_context, inventory_cli):
    result = inventory_cli._graph_group(mock_group)
    assert result == ['@test_group:']

def test_graph_group_with_children(mock_group, mock_context, inventory_cli):
    child_group = MagicMock()
    child_group.name = 'child_group'
    child_group.child_groups = []
    child_group.hosts = []
    mock_group.child_groups = [child_group]
    
    result = inventory_cli._graph_group(mock_group)
    assert result == ['@test_group:', '  |--@child_group:']

def test_graph_group_with_hosts(mock_group, mock_host, mock_context, inventory_cli):
    mock_group.hosts = [mock_host]
    
    result = inventory_cli._graph_group(mock_group)
    assert result == ['@test_group:', '  |--test_host']

def test_graph_group_with_show_vars(mock_group, mock_host, inventory_cli):
    with patch('ansible.context.CLIARGS', {'show_vars': True, 'export': False, 'basedir': None}):
        mock_group.hosts = [mock_host]
        mock_group.get_vars.return_value = {'var1': 'value1'}
        mock_host.get_vars.return_value = {'var2': 'value2'}
        
        with patch.object(inventory_cli, '_get_host_variables', return_value={'var2': 'value2'}):
            with patch.object(inventory_cli, '_get_group_variables', return_value={'var1': 'value1'}):
                result = inventory_cli._graph_group(mock_group)
                assert result == [
                    '@test_group:',
                    '  |--test_host',
                    '  |  |--{var2 = value2}',
                    '  |--{var1 = value1}'
                ]
