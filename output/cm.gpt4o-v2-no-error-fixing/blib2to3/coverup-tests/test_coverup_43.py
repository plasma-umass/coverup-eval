# file: src/blib2to3/pytree.py:314-318
# asked: {"lines": [314, 316, 317, 318], "branches": [[317, 0], [317, 318]]}
# gained: {"lines": [314, 316, 317, 318], "branches": [[317, 0], [317, 318]]}

import pytest
from blib2to3.pytree import Node
from typing import List

class MockChild(Node):
    def __init__(self, type: int, children: List[Node] = []):
        super().__init__(type, children)

def test_pre_order():
    # Create a mock tree structure
    child1 = MockChild(256, [])
    child2 = MockChild(256, [])
    root = MockChild(256, [child1, child2])

    # Collect nodes in pre-order
    result = list(root.pre_order())

    # Verify the order is root, child1, child2
    assert result == [root, child1, child2]

    # Clean up
    del root, child1, child2, result
