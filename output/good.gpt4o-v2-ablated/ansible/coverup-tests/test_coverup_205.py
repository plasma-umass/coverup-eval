# file: lib/ansible/cli/inventory.py:260-264
# asked: {"lines": [260, 261, 262, 263, 264], "branches": [[262, 263], [262, 264]]}
# gained: {"lines": [260, 261, 262, 263, 264], "branches": [[262, 263], [262, 264]]}

import pytest
from ansible.cli.inventory import InventoryCLI

@pytest.mark.parametrize("name, depth, expected", [
    ("host1", 0, "host1"),
    ("host2", 1, "  |--host2"),
    ("host3", 2, "  |  |--host3"),
    ("host4", 3, "  |  |  |--host4"),
])
def test_graph_name(name, depth, expected):
    result = InventoryCLI._graph_name(name, depth)
    assert result == expected
