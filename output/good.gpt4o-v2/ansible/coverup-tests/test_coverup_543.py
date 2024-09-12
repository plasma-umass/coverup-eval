# file: lib/ansible/cli/inventory.py:284-290
# asked: {"lines": [284, 286, 287, 288, 290], "branches": [[287, 288], [287, 290]]}
# gained: {"lines": [284, 286, 287, 288, 290], "branches": [[287, 288], [287, 290]]}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.cli.inventory import InventoryCLI
from ansible import context

@pytest.fixture
def inventory_cli(mocker):
    args = ['some', 'args']
    cli = InventoryCLI(args)
    mocker.patch.object(cli, '_get_group')
    mocker.patch.object(cli, '_graph_group')
    return cli

def test_inventory_graph_valid_group(inventory_cli, mocker):
    context.CLIARGS = {'pattern': 'valid_group'}
    inventory_cli._get_group.return_value = mocker.Mock(name='valid_group')
    inventory_cli._graph_group.return_value = ['group1', 'group2']

    result = inventory_cli.inventory_graph()

    inventory_cli._get_group.assert_called_once_with('valid_group')
    inventory_cli._graph_group.assert_called_once_with(inventory_cli._get_group.return_value)
    assert result == 'group1\ngroup2'

def test_inventory_graph_invalid_group(inventory_cli, mocker):
    context.CLIARGS = {'pattern': 'invalid_group'}
    inventory_cli._get_group.return_value = None

    with pytest.raises(AnsibleOptionsError, match="Pattern must be valid group name when using --graph"):
        inventory_cli.inventory_graph()

    inventory_cli._get_group.assert_called_once_with('invalid_group')
