# file: src/blib2to3/pytree.py:369-379
# asked: {"lines": [369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[375, 376], [375, 379]]}
# gained: {"lines": [369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[375, 376], [375, 379]]}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None

def test_update_sibling_maps():
    # Create mock children
    child1 = MockChild()
    child2 = MockChild()
    child3 = MockChild()
    
    # Create a Node with these children
    node = Node(type=256, children=[child1, child2, child3])
    
    # Call update_sibling_maps
    node.update_sibling_maps()
    
    # Assertions to verify the sibling maps
    assert node.prev_sibling_map[id(child1)] is None
    assert node.prev_sibling_map[id(child2)] == child1
    assert node.prev_sibling_map[id(child3)] == child2
    
    assert node.next_sibling_map[id(child1)] == child2
    assert node.next_sibling_map[id(child2)] == child3
    assert node.next_sibling_map[id(child3)] is None

    # Clean up
    del node
    del child1
    del child2
    del child3
