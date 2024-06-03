# file lib/ansible/cli/inventory.py:260-264
# lines [260, 261, 262, 263, 264]
# branches ['262->263', '262->264']

import pytest
from ansible.cli.inventory import InventoryCLI

def test_graph_name():
    # Test with depth 0
    name = "test"
    result = InventoryCLI._graph_name(name, depth=0)
    assert result == "test", f"Expected 'test', got {result}"

    # Test with depth 1
    result = InventoryCLI._graph_name(name, depth=1)
    assert result == "  |--test", f"Expected '  |--test', got {result}"

    # Test with depth 2
    result = InventoryCLI._graph_name(name, depth=2)
    assert result == "  |  |--test", f"Expected '  |  |--test', got {result}"

    # Test with depth 3
    result = InventoryCLI._graph_name(name, depth=3)
    assert result == "  |  |  |--test", f"Expected '  |  |  |--test', got {result}"
