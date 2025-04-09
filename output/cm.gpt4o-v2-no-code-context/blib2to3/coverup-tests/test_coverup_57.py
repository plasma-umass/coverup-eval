# file: src/blib2to3/pytree.py:355-363
# asked: {"lines": [355, 360, 361, 362, 363], "branches": []}
# gained: {"lines": [355, 360, 361, 362, 363], "branches": []}

import pytest
from blib2to3.pytree import Node, Leaf
from blib2to3.pgen2 import token

class MockNode:
    def __init__(self):
        self.parent = None

@pytest.fixture
def node():
    return Node(type=256, children=[])

def test_append_child(node, mocker):
    child = MockNode()
    mock_changed = mocker.patch.object(node, 'changed')
    mock_invalidate_sibling_maps = mocker.patch.object(node, 'invalidate_sibling_maps')
    
    node.append_child(child)
    
    assert child.parent == node
    assert child in node.children
    mock_changed.assert_called_once()
    mock_invalidate_sibling_maps.assert_called_once()
