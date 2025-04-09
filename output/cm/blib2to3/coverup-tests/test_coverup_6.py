# file src/blib2to3/pgen2/parse.py:205-217
# lines [205, 209, 210, 211, 212, 213, 214, 215, 216, 217]
# branches ['214->215', '214->217']

import pytest
from typing import Optional, Text, Tuple
from blib2to3.pgen2 import grammar
from blib2to3.pgen2.parse import Parser

class DummyDFA:
    def __init__(self):
        pass

class DummyNode:
    def __init__(self):
        self.children = []

    def append(self, node):
        self.children.append(node)

@pytest.fixture
def parser():
    g = grammar.Grammar()
    p = Parser(g)
    p.stack = [(DummyDFA(), 0, [DummyNode()])]
    return p

def test_parser_shift_with_newnode(parser, mocker):
    mocker.patch.object(parser, 'convert', return_value=DummyNode())
    type = 1
    value = "value"
    newstate = 2
    context = ("", 0, 0, 0)
    parser.shift(type, value, newstate, context)
    dfa, state, node = parser.stack[-1]
    assert state == newstate
    assert len(node[-1].children) == 1

def test_parser_shift_with_none_node(parser, mocker):
    mocker.patch.object(parser, 'convert', return_value=None)
    type = 1
    value = "value"
    newstate = 2
    context = ("", 0, 0, 0)
    parser.shift(type, value, newstate, context)
    dfa, state, node = parser.stack[-1]
    assert state == newstate
    assert len(node[-1].children) == 0
