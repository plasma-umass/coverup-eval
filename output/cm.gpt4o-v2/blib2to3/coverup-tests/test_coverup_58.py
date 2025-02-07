# file: src/blib2to3/pytree.py:365-367
# asked: {"lines": [365, 366, 367], "branches": []}
# gained: {"lines": [365, 366, 367], "branches": []}

import pytest
from blib2to3.pytree import Node

def test_invalidate_sibling_maps():
    # Create a Node instance with required arguments
    node = Node(type=256, children=[])
    
    # Set up initial state
    node.prev_sibling_map = {1: None}
    node.next_sibling_map = {1: None}
    
    # Call the method to test
    node.invalidate_sibling_maps()
    
    # Assert the postconditions
    assert node.prev_sibling_map is None
    assert node.next_sibling_map is None
