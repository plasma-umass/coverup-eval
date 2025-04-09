# file: src/blib2to3/pytree.py:345-353
# asked: {"lines": [345, 350, 351, 352, 353], "branches": []}
# gained: {"lines": [345, 350, 351, 352, 353], "branches": []}

import pytest
from blib2to3.pytree import Node, Base

class MockNode(Node):
    def __init__(self):
        self.children = []
        self._changed = False
        self._sibling_maps_invalidated = False

    def changed(self):
        self._changed = True

    def invalidate_sibling_maps(self):
        self._sibling_maps_invalidated = True

def test_insert_child():
    parent = MockNode()
    child = MockNode()
    
    parent.insert_child(0, child)
    
    assert child.parent is parent
    assert parent.children[0] is child
    assert parent._changed
    assert parent._sibling_maps_invalidated
