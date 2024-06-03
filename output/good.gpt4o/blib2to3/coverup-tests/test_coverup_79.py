# file src/blib2to3/pytree.py:369-379
# lines [370, 371, 372, 373, 374, 375, 376, 377, 378, 379]
# branches ['375->376', '375->379']

import pytest
from blib2to3.pytree import Node

def test_update_sibling_maps():
    class TestNode(Node):
        def __init__(self, children):
            self.children = children

    # Create mock children nodes
    child1 = TestNode([])
    child2 = TestNode([])
    child3 = TestNode([])

    # Create a parent node with children
    parent = TestNode([child1, child2, child3])

    # Call the method to be tested
    parent.update_sibling_maps()

    # Assertions to verify the sibling maps
    assert parent.prev_sibling_map[id(child1)] is None
    assert parent.prev_sibling_map[id(child2)] is child1
    assert parent.prev_sibling_map[id(child3)] is child2

    assert parent.next_sibling_map[id(child1)] is child2
    assert parent.next_sibling_map[id(child2)] is child3
    assert parent.next_sibling_map[id(child3)] is None
