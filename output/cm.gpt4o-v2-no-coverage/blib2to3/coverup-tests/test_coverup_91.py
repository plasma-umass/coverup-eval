# file: src/blib2to3/pgen2/parse.py:37-39
# asked: {"lines": [38, 39], "branches": []}
# gained: {"lines": [38, 39], "branches": []}

import pytest
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pytree import NL, Node
from blib2to3.pgen2.parse import lam_sub

def test_lam_sub():
    grammar = Grammar()
    node = (256, None, None, [Node(256, [], None)])
    
    result = lam_sub(grammar, node)
    
    assert isinstance(result, Node)
    assert result.type == 256
    assert result.children == node[3]
    assert result.prefix == ''
