# file: lib/ansible/cli/inventory.py:266-282
# asked: {"lines": [268, 269, 270, 271, 273, 274, 275, 276, 277, 279, 280, 282], "branches": [[270, 271], [270, 273], [273, 274], [273, 279], [274, 275], [274, 279], [276, 274], [276, 277], [279, 280], [279, 282]]}
# gained: {"lines": [268, 269, 270, 271, 273, 274, 275, 276, 277, 279, 280, 282], "branches": [[270, 271], [270, 273], [273, 274], [274, 275], [274, 279], [276, 274], [276, 277], [279, 280], [279, 282]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from operator import attrgetter

@pytest.fixture
def mock_context(mocker):
    mocker.patch('ansible.cli.inventory.context.CLIARGS', {'show_vars': False})

@pytest.fixture
def mock_context_show_vars(mocker):
    mocker.patch('ansible.cli.inventory.context.CLIARGS', {'show_vars': True})

@pytest.fixture
def inventory_cli(mocker):
    mocker.patch('ansible.cli.inventory.CLI.__init__', return_value=None)
    return InventoryCLI(args=[])

@pytest.fixture
def group():
    group = Group('test_group')
    child_group = Group('child_group')
    host = Host('test_host')
    child_group.add_host(host)
    group.add_child_group(child_group)
    return group

def test_graph_group_no_show_vars(inventory_cli, group, mock_context):
    result = inventory_cli._graph_group(group)
    assert '@test_group:' in result
    assert '  |--@child_group:' in result
    assert '  |  |--test_host' in result

def test_graph_group_show_vars(inventory_cli, group, mock_context_show_vars, mocker):
    mocker.patch.object(inventory_cli, '_get_host_variables', return_value={'var1': 'value1'})
    mocker.patch.object(inventory_cli, '_get_group_variables', return_value={'var2': 'value2'})
    mocker.patch.object(inventory_cli, '_show_vars', side_effect=lambda vars, depth: [f'{k}: {v}' for k, v in vars.items()])

    result = inventory_cli._graph_group(group)
    assert '@test_group:' in result
    assert '  |--@child_group:' in result
    assert '  |  |--test_host' in result
    assert 'var1: value1' in result
    assert 'var2: value2' in result
