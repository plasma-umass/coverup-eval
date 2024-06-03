# file src/blib2to3/pytree.py:355-363
# lines [360, 361, 362, 363]
# branches []

import pytest
from blib2to3.pytree import Node, Leaf
from blib2to3.pgen2.grammar import Grammar

class MockChild:
    def __init__(self):
        self.parent = None

@pytest.fixture
def mock_node(mocker):
    grammar = Grammar()
    node = Node(type=256, children=[], context=grammar)
    mocker.patch.object(node, 'changed')
    mocker.patch.object(node, 'invalidate_sibling_maps')
    return node

def test_append_child(mock_node):
    child = MockChild()
    mock_node.append_child(child)
    
    assert child.parent is mock_node
    assert child in mock_node.children
    mock_node.changed.assert_called_once()
    mock_node.invalidate_sibling_maps.assert_called_once()
