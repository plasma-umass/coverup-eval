# file: src/blib2to3/pytree.py:478-495
# asked: {"lines": [493], "branches": [[491, 493]]}
# gained: {"lines": [493], "branches": [[491, 493]]}

import pytest
from blib2to3.pytree import convert, Node, Leaf
from blib2to3.pgen2.grammar import Grammar

def test_convert_to_node():
    # Mock Grammar
    class MockGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.number2symbol = {256: 'symbol'}
    
    gr = MockGrammar()
    raw_node = (256, None, None, [Node(256, [Leaf(1, 'value')]), Leaf(1, 'value2')])

    result = convert(gr, raw_node)
    
    assert isinstance(result, Node)
    assert result.type == 256
    assert len(result.children) == 2
    assert isinstance(result.children[0], Node)
    assert isinstance(result.children[1], Leaf)
    assert result.children[0].children[0].value == 'value'
    assert result.children[1].value == 'value2'

def test_convert_to_leaf():
    # Mock Grammar
    class MockGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.number2symbol = {}

    gr = MockGrammar()
    raw_node = (1, 'value', None, None)

    result = convert(gr, raw_node)
    
    assert isinstance(result, Leaf)
    assert result.type == 1
    assert result.value == 'value'
