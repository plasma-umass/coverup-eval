# file src/blib2to3/pgen2/parse.py:119-141
# lines [119, 132, 133, 137, 138, 139, 140, 141]
# branches ['132->133', '132->137']

import pytest
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar():
    # Minimal grammar setup for testing
    g = Grammar()
    g.start = 256  # Assign an arbitrary start symbol
    g.dfas[256] = (None, None)  # Minimal DFA for the start symbol
    return g

@pytest.fixture
def parser(grammar):
    return Parser(grammar)

def test_parser_setup_with_default_start(grammar, parser):
    # Test setup with default start symbol
    parser.setup()
    assert len(parser.stack) == 1
    assert parser.stack[0][0] == (None, None)  # DFA as set in grammar fixture
    assert parser.stack[0][1] == 0  # State is 0 as initialized
    assert parser.stack[0][2][0] == grammar.start  # Node type is the grammar's start symbol
    assert parser.stack[0][2][1] is None  # Node value is None
    assert parser.stack[0][2][2] is None  # Node context is None
    assert parser.stack[0][2][3] == []  # Node children is an empty list
    assert parser.rootnode is None
    assert parser.used_names == set()

def test_parser_setup_with_explicit_start(grammar, parser):
    # Test setup with an explicit start symbol
    explicit_start = 257  # Assign an arbitrary explicit start symbol
    grammar.dfas[explicit_start] = (None, None)  # Minimal DFA for the explicit start symbol
    parser.setup(explicit_start)
    assert len(parser.stack) == 1
    assert parser.stack[0][0] == (None, None)  # DFA as set in grammar fixture
    assert parser.stack[0][1] == 0  # State is 0 as initialized
    assert parser.stack[0][2][0] == explicit_start  # Node type is the explicit start symbol
    assert parser.stack[0][2][1] is None  # Node value is None
    assert parser.stack[0][2][2] is None  # Node context is None
    assert parser.stack[0][2][3] == []  # Node children is an empty list
    assert parser.rootnode is None
    assert parser.used_names == set()
