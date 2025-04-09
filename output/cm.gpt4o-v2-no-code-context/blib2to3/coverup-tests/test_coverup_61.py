# file: src/blib2to3/pytree.py:345-353
# asked: {"lines": [345, 350, 351, 352, 353], "branches": []}
# gained: {"lines": [345, 350, 351, 352, 353], "branches": []}

import pytest
from blib2to3.pytree import Node, Leaf

class MockChild:
    def __init__(self):
        self.parent = None

@pytest.fixture
def node():
    return Node(type=256, children=[])

@pytest.fixture
def child():
    return MockChild()

def test_insert_child(node, child, mocker):
    # Mock the methods that are called within insert_child
    mocker.patch.object(node, 'changed')
    mocker.patch.object(node, 'invalidate_sibling_maps')
    
    # Call the method
    node.insert_child(0, child)

    # Assertions to verify postconditions
    assert child.parent == node
    assert node.children[0] == child
    node.changed.assert_called_once()
    node.invalidate_sibling_maps.assert_called_once()
