# file: src/blib2to3/pgen2/parse.py:219-224
# asked: {"lines": [219, 221, 222, 223, 224], "branches": []}
# gained: {"lines": [219, 221, 222, 223, 224], "branches": []}

import pytest
from blib2to3.pgen2.parse import Parser, DFAS, Context
from blib2to3.pgen2.grammar import Grammar

class MockDFAS:
    pass

class MockContext:
    pass

@pytest.fixture
def parser():
    grammar = Grammar()
    p = Parser(grammar)
    p.stack = [(MockDFAS(), 0, None)]
    return p

def test_push(parser):
    newdfa = MockDFAS()
    newstate = 1
    context = MockContext()
    type = 42

    parser.push(type, newdfa, newstate, context)

    assert len(parser.stack) == 2
    assert parser.stack[0][1] == newstate
    assert parser.stack[1][0] == newdfa
    assert parser.stack[1][1] == 0
    assert parser.stack[1][2][0] == type
    assert parser.stack[1][2][2] == context
    assert parser.stack[1][2][3] == []
