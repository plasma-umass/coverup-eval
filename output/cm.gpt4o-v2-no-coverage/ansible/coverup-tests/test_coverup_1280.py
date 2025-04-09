# file: lib/ansible/cli/inventory.py:284-290
# asked: {"lines": [286, 287, 288, 290], "branches": [[287, 288], [287, 290]]}
# gained: {"lines": [286, 287, 288, 290], "branches": [[287, 288], [287, 290]]}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.cli.inventory import InventoryCLI
from ansible import context

class MockCLIArgs:
    def __init__(self, pattern):
        self.CLIARGS = {'pattern': pattern}

@pytest.fixture
def mock_context(monkeypatch):
    def mock_get_group(pattern):
        if pattern == "valid_group":
            return ["group1", "group2"]
        return None

    monkeypatch.setattr(context, 'CLIARGS', MockCLIArgs('valid_group').CLIARGS)
    monkeypatch.setattr(InventoryCLI, '_get_group', lambda self, x: mock_get_group(x))
    monkeypatch.setattr(InventoryCLI, '_graph_group', lambda self, x: x)

def test_inventory_graph_valid_group(mock_context):
    cli = InventoryCLI(['some_arg'])
    result = cli.inventory_graph()
    assert result == 'group1\ngroup2'

def test_inventory_graph_invalid_group(monkeypatch):
    monkeypatch.setattr(context, 'CLIARGS', MockCLIArgs('invalid_group').CLIARGS)
    monkeypatch.setattr(InventoryCLI, '_get_group', lambda self, x: None)
    
    cli = InventoryCLI(['some_arg'])
    with pytest.raises(AnsibleOptionsError, match="Pattern must be valid group name when using --graph"):
        cli.inventory_graph()
