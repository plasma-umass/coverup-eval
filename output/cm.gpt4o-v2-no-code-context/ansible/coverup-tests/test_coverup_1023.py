# file: lib/ansible/cli/inventory.py:284-290
# asked: {"lines": [286, 287, 288, 290], "branches": [[287, 288], [287, 290]]}
# gained: {"lines": [286, 287, 288, 290], "branches": [[287, 288], [287, 290]]}

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleOptionsError
from unittest.mock import patch

@pytest.fixture
def inventory_cli(mocker):
    mocker.patch('ansible.cli.inventory.CLI.__init__', return_value=None)
    return InventoryCLI(args=[])

def test_inventory_graph_valid_group(mocker, inventory_cli):
    mocker.patch('ansible.cli.inventory.InventoryCLI._get_group', return_value='valid_group')
    mocker.patch('ansible.cli.inventory.InventoryCLI._graph_group', return_value=['group1', 'group2'])
    mocker.patch('ansible.cli.inventory.context.CLIARGS', {'pattern': 'some_pattern'})

    result = inventory_cli.inventory_graph()
    assert result == 'group1\ngroup2'

def test_inventory_graph_invalid_group(mocker, inventory_cli):
    mocker.patch('ansible.cli.inventory.InventoryCLI._get_group', return_value=None)
    mocker.patch('ansible.cli.inventory.context.CLIARGS', {'pattern': 'some_pattern'})

    with pytest.raises(AnsibleOptionsError, match="Pattern must be valid group name when using --graph"):
        inventory_cli.inventory_graph()
