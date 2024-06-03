# file src/blib2to3/pytree.py:345-353
# lines [345, 350, 351, 352, 353]
# branches []

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None

@pytest.fixture
def node():
    class TestNode(Node):
        def __init__(self):
            self.children = []
            self._changed = False
            self._sibling_maps_invalidated = False

        def changed(self):
            self._changed = True

        def invalidate_sibling_maps(self):
            self._sibling_maps_invalidated = True

    return TestNode()

def test_insert_child(node):
    child = MockChild()
    node.insert_child(0, child)

    assert child.parent is node
    assert node.children == [child]
    assert node._changed
    assert node._sibling_maps_invalidated
