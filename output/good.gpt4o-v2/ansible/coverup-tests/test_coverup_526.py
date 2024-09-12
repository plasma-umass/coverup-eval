# file: lib/ansible/cli/inventory.py:260-264
# asked: {"lines": [260, 261, 262, 263, 264], "branches": [[262, 263], [262, 264]]}
# gained: {"lines": [260, 261, 262, 263, 264], "branches": [[262, 263], [262, 264]]}

import pytest
from ansible.cli.inventory import InventoryCLI

def test_graph_name_no_depth():
    name = "test"
    result = InventoryCLI._graph_name(name)
    assert result == "test"

def test_graph_name_with_depth():
    name = "test"
    depth = 2
    result = InventoryCLI._graph_name(name, depth)
    assert result == "  |  |--test"
