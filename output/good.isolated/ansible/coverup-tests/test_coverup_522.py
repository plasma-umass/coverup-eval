# file lib/ansible/cli/inventory.py:260-264
# lines [260, 261, 262, 263, 264]
# branches ['262->263', '262->264']

import pytest
from ansible.cli.inventory import InventoryCLI

# Test function for InventoryCLI._graph_name
def test_graph_name_depth():
    # Test with depth 0
    name = "test_node"
    assert InventoryCLI._graph_name(name) == "test_node", "Name should be unchanged with depth 0"

    # Test with depth 1
    assert InventoryCLI._graph_name(name, depth=1) == "  |--test_node", "Name should be indented once with depth 1"

    # Test with depth 2
    assert InventoryCLI._graph_name(name, depth=2) == "  |  |--test_node", "Name should be indented twice with depth 2"

    # Test with depth 3
    assert InventoryCLI._graph_name(name, depth=3) == "  |  |  |--test_node", "Name should be indented thrice with depth 3"

# This test does not require any cleanup, as it does not modify any external state.
