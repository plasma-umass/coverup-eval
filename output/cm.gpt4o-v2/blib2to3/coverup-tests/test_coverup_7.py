# file: src/blib2to3/pytree.py:478-495
# asked: {"lines": [478, 486, 487, 490, 491, 492, 493, 495], "branches": [[487, 490], [487, 495], [491, 492], [491, 493]]}
# gained: {"lines": [478, 486, 487, 490, 491, 492, 495], "branches": [[487, 490], [487, 495], [491, 492]]}

import pytest
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pytree import convert, Node, Leaf

@pytest.fixture
def grammar():
    gr = Grammar()
    gr.number2symbol = {256: 'symbol'}
    return gr

def test_convert_with_children(grammar):
    raw_node = (256, 'value', ('', (1, 0)), [Node(256, [], context=None)])
    result = convert(grammar, raw_node)
    assert isinstance(result, Node)
    assert result.type == 256
    assert result.children == []

def test_convert_with_single_child(grammar):
    child_node = Node(256, [], context=None)
    raw_node = (256, 'value', ('', (1, 0)), [child_node])
    result = convert(grammar, raw_node)
    assert result is child_node

def test_convert_without_children(grammar):
    raw_node = (1, 'value', ('', (1, 0)), [])
    result = convert(grammar, raw_node)
    assert isinstance(result, Leaf)
    assert result.type == 1
    assert result.value == 'value'
