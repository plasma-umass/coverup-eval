# file: lib/ansible/cli/inventory.py:260-264
# asked: {"lines": [260, 261, 262, 263, 264], "branches": [[262, 263], [262, 264]]}
# gained: {"lines": [260, 261, 262, 263, 264], "branches": [[262, 263], [262, 264]]}

import pytest
from ansible.cli.inventory import InventoryCLI

def test_graph_name_no_depth():
    result = InventoryCLI._graph_name("test_name")
    assert result == "test_name"

def test_graph_name_with_depth():
    result = InventoryCLI._graph_name("test_name", depth=2)
    assert result == "  |  |--test_name"
