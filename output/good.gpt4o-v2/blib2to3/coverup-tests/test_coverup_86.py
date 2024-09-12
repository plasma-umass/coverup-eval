# file: src/blib2to3/pytree.py:206-218
# asked: {"lines": [212, 213, 215, 216, 217, 218], "branches": [[212, 213], [212, 215], [215, 216], [215, 217]]}
# gained: {"lines": [212, 213, 215, 216, 217, 218], "branches": [[212, 213], [212, 215], [215, 216], [215, 217]]}

import pytest
from unittest.mock import Mock
from blib2to3.pytree import Node

def test_prev_sibling_no_parent():
    node = Node(256, [])
    node.parent = None
    assert node.prev_sibling is None

def test_prev_sibling_no_sibling_map():
    node = Node(256, [])
    parent = Node(256, [node])
    parent.prev_sibling_map = None
    parent.update_sibling_maps = Mock()
    parent.update_sibling_maps.side_effect = lambda: setattr(parent, 'prev_sibling_map', {id(node): None})
    
    assert node.prev_sibling is None
    parent.update_sibling_maps.assert_called_once()

def test_prev_sibling_with_sibling_map():
    sibling = Node(256, [])
    node = Node(256, [])
    parent = Node(256, [sibling, node])
    parent.prev_sibling_map = {id(node): sibling}
    
    assert node.prev_sibling is sibling
