# file: src/blib2to3/pgen2/parse.py:119-141
# asked: {"lines": [119, 132, 133, 137, 138, 139, 140, 141], "branches": [[132, 133], [132, 137]]}
# gained: {"lines": [119, 132, 133, 137, 138, 139, 140, 141], "branches": [[132, 133], [132, 137]]}

import pytest
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def mock_grammar():
    grammar = Grammar()
    grammar.start = 256  # Arbitrary start symbol
    grammar.dfas = {256: (None, None)}  # Minimal DFA structure
    return grammar

@pytest.fixture
def parser(mock_grammar):
    return Parser(mock_grammar)

def test_parser_setup_with_default_start(parser):
    parser.setup()
    assert parser.stack[0][0] == parser.grammar.dfas[parser.grammar.start]
    assert parser.stack[0][1] == 0
    assert parser.stack[0][2] == (parser.grammar.start, None, None, [])
    assert parser.rootnode is None
    assert parser.used_names == set()

def test_parser_setup_with_custom_start(parser):
    custom_start = 300  # Arbitrary custom start symbol
    parser.grammar.dfas[custom_start] = (None, None)  # Add custom DFA
    parser.setup(start=custom_start)
    assert parser.stack[0][0] == parser.grammar.dfas[custom_start]
    assert parser.stack[0][1] == 0
    assert parser.stack[0][2] == (custom_start, None, None, [])
    assert parser.rootnode is None
    assert parser.used_names == set()
