# file: src/blib2to3/pytree.py:355-363
# asked: {"lines": [355, 360, 361, 362, 363], "branches": []}
# gained: {"lines": [355, 360, 361, 362, 363], "branches": []}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self):
        self.parent = None

@pytest.fixture
def node(mocker):
    node = Node(type=256, children=[])
    mocker.patch.object(node, 'changed')
    mocker.patch.object(node, 'invalidate_sibling_maps')
    return node

def test_append_child(node):
    child = MockChild()
    node.append_child(child)
    
    assert child.parent == node
    assert child in node.children

    node.changed.assert_called_once()
    node.invalidate_sibling_maps.assert_called_once()
