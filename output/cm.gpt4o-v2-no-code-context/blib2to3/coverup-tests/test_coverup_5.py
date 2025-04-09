# file: src/blib2to3/pytree.py:369-379
# asked: {"lines": [369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[375, 376], [375, 379]]}
# gained: {"lines": [369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[375, 376], [375, 379]]}

import pytest
from blib2to3.pytree import Node, Leaf

def test_update_sibling_maps():
    # Create a mock Node class with children
    class MockNode(Node):
        def __init__(self, children):
            self.children = children

    # Create some mock children nodes
    child1 = Leaf(1, "child1")
    child2 = Leaf(2, "child2")
    child3 = Leaf(3, "child3")

    # Create a node with children
    node = MockNode([child1, child2, child3])

    # Call the method to be tested
    node.update_sibling_maps()

    # Assertions to verify the sibling maps
    assert node.prev_sibling_map[id(child1)] is None
    assert node.prev_sibling_map[id(child2)] == child1
    assert node.prev_sibling_map[id(child3)] == child2

    assert node.next_sibling_map[id(child1)] == child2
    assert node.next_sibling_map[id(child2)] == child3
    assert node.next_sibling_map[id(child3)] is None
