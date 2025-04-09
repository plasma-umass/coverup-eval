# file: src/blib2to3/pytree.py:365-367
# asked: {"lines": [365, 366, 367], "branches": []}
# gained: {"lines": [365, 366, 367], "branches": []}

import pytest
from blib2to3.pytree import Node, Leaf

@pytest.fixture
def node_instance():
    # Create a Node instance with required arguments
    return Node(type=256, children=[Leaf(1, 'test')])

def test_invalidate_sibling_maps(node_instance):
    # Set up initial state
    node_instance.prev_sibling_map = {1: None}
    node_instance.next_sibling_map = {1: None}
    
    # Call the method to test
    node_instance.invalidate_sibling_maps()
    
    # Assertions to verify postconditions
    assert node_instance.prev_sibling_map is None
    assert node_instance.next_sibling_map is None
