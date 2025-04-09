# file: src/blib2to3/pytree.py:314-318
# asked: {"lines": [314, 316, 317, 318], "branches": [[317, 0], [317, 318]]}
# gained: {"lines": [314, 316, 317, 318], "branches": [[317, 0], [317, 318]]}

import pytest
from blib2to3.pytree import Node

def test_pre_order():
    # Create a mock Node class with children attribute
    class MockNode(Node):
        def __init__(self, children=None):
            self.children = children or []

    # Create a tree structure
    leaf1 = MockNode()
    leaf2 = MockNode()
    child = MockNode(children=[leaf1, leaf2])
    root = MockNode(children=[child])

    # Collect nodes in pre-order
    result = list(root.pre_order())

    # Verify the order and content of the nodes
    assert result == [root, child, leaf1, leaf2]

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # No specific cleanup needed in this case
