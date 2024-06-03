# file src/blib2to3/pytree.py:365-367
# lines [365, 366, 367]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf

def test_invalidate_sibling_maps():
    node = Node(type=256, children=[])
    node.prev_sibling_map = {1: None}
    node.next_sibling_map = {2: None}
    
    node.invalidate_sibling_maps()
    
    assert node.prev_sibling_map is None
    assert node.next_sibling_map is None
