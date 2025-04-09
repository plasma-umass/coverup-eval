# file: lib/ansible/cli/inventory.py:284-290
# asked: {"lines": [284, 286, 287, 288, 290], "branches": [[287, 288], [287, 290]]}
# gained: {"lines": [284, 286, 287, 288, 290], "branches": [[287, 288], [287, 290]]}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.cli.inventory import InventoryCLI
from unittest.mock import MagicMock

@pytest.fixture
def inventory_cli():
    cli = InventoryCLI(MagicMock())
    cli._get_group = MagicMock()
    cli._graph_group = MagicMock()
    return cli

def test_inventory_graph_valid_group(inventory_cli, monkeypatch):
    monkeypatch.setattr('ansible.context.CLIARGS', {'pattern': 'valid_group'})
    inventory_cli._get_group.return_value = MagicMock(name='valid_group')
    inventory_cli._graph_group.return_value = ['group1', 'group2']

    result = inventory_cli.inventory_graph()

    inventory_cli._get_group.assert_called_once_with('valid_group')
    inventory_cli._graph_group.assert_called_once()
    assert result == 'group1\ngroup2'

def test_inventory_graph_invalid_group(inventory_cli, monkeypatch):
    monkeypatch.setattr('ansible.context.CLIARGS', {'pattern': 'invalid_group'})
    inventory_cli._get_group.return_value = None

    with pytest.raises(AnsibleOptionsError, match="Pattern must be valid group name when using --graph"):
        inventory_cli.inventory_graph()

    inventory_cli._get_group.assert_called_once_with('invalid_group')
