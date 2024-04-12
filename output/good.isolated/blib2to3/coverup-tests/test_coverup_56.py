# file src/blib2to3/pytree.py:365-367
# lines [365, 366, 367]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf

def test_invalidate_sibling_maps(mocker):
    # Mocking the Node class to avoid TypeError due to missing required arguments
    mocker.patch.object(Node, '__init__', return_value=None)
    
    node = Node()
    node.prev_sibling_map = {1: None}
    node.next_sibling_map = {2: None}

    # Ensure the maps are not None before invalidation
    assert node.prev_sibling_map is not None
    assert node.next_sibling_map is not None

    # Call the method that should invalidate the maps
    node.invalidate_sibling_maps()

    # Ensure the maps are None after invalidation
    assert node.prev_sibling_map is None
    assert node.next_sibling_map is None
