# file lib/ansible/cli/inventory.py:284-290
# lines [284, 286, 287, 288, 290]
# branches ['287->288', '287->290']

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleOptionsError
from unittest.mock import MagicMock

# Assuming context is a module that needs to be imported
from ansible import context

@pytest.fixture
def inventory_cli(mocker):
    mocker.patch('ansible.cli.inventory.CLI.__init__', return_value=None)
    cli = InventoryCLI([])
    cli._get_group = MagicMock()
    cli._graph_group = MagicMock()
    return cli

def test_inventory_graph_with_valid_group(inventory_cli):
    # Setup the context and mock return values
    context.CLIARGS = {'pattern': 'valid_group'}
    inventory_cli._get_group.return_value = 'valid_group'
    inventory_cli._graph_group.return_value = ['group1', 'group2']

    # Call the method
    graph_output = inventory_cli.inventory_graph()

    # Assertions to check the output
    assert graph_output == 'group1\ngroup2'
    inventory_cli._get_group.assert_called_once_with('valid_group')
    inventory_cli._graph_group.assert_called_once_with('valid_group')

def test_inventory_graph_with_invalid_group(inventory_cli):
    # Setup the context and mock return values
    context.CLIARGS = {'pattern': 'invalid_group'}
    inventory_cli._get_group.return_value = None

    # Call the method and assert it raises an error
    with pytest.raises(AnsibleOptionsError) as excinfo:
        inventory_cli.inventory_graph()

    # Check the exception message
    assert "Pattern must be valid group name when using --graph" in str(excinfo.value)
    inventory_cli._get_group.assert_called_once_with('invalid_group')
