# file: src/blib2to3/pytree.py:478-495
# asked: {"lines": [478, 486, 487, 490, 491, 492, 493, 495], "branches": [[487, 490], [487, 495], [491, 492], [491, 493]]}
# gained: {"lines": [478, 486, 487, 490, 491, 492, 493, 495], "branches": [[487, 490], [487, 495], [491, 492], [491, 493]]}

import pytest
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pytree import convert, Node, Leaf

@pytest.fixture
def grammar():
    gr = Grammar()
    gr.number2symbol = {256: 'symbol'}
    return gr

def test_convert_to_node(grammar):
    raw_node = (256, None, None, [Node(256, [])])
    result = convert(grammar, raw_node)
    assert isinstance(result, Node)
    assert result.type == 256

def test_convert_to_leaf(grammar):
    raw_node = (1, 'value', None, None)
    result = convert(grammar, raw_node)
    assert isinstance(result, Leaf)
    assert result.type == 1
    assert result.value == 'value'

def test_convert_single_child(grammar):
    child_node = Node(256, [])
    raw_node = (256, None, None, [child_node])
    result = convert(grammar, raw_node)
    assert result is child_node

def test_convert_multiple_children(grammar):
    child_node1 = Node(256, [])
    child_node2 = Node(256, [])
    raw_node = (256, None, None, [child_node1, child_node2])
    result = convert(grammar, raw_node)
    assert isinstance(result, Node)
    assert result.children == [child_node1, child_node2]
