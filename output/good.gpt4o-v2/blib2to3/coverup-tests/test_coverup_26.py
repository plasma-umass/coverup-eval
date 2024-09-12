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
    child1 = MockChild(256)
    child2 = MockChild(256)
    parent = MockChild(256, [child1, child2])

    # Collect nodes in pre-order
    result = list(parent.pre_order())

    # Assert the order is correct
    assert result == [parent, child1, child2]

    # Clean up
    del parent
    del child1
    del child2
    del result
