# file: src/blib2to3/pgen2/parse.py:119-141
# asked: {"lines": [119, 132, 133, 137, 138, 139, 140, 141], "branches": [[132, 133], [132, 137]]}
# gained: {"lines": [119, 132, 133, 137, 138, 139, 140, 141], "branches": [[132, 133], [132, 137]]}

import pytest
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pytree import NL, RawNode

@pytest.fixture
def grammar():
    class MockGrammar:
        start = 256
        dfas = {256: 'mock_dfa', 300: 'mock_dfa_300'}
    return MockGrammar()

def test_parser_setup_with_start(grammar):
    parser = Parser(grammar)
    parser.setup(start=300)
    
    assert parser.stack == [(grammar.dfas[300], 0, (300, None, None, []))]
    assert parser.rootnode is None
    assert parser.used_names == set()

def test_parser_setup_without_start(grammar):
    parser = Parser(grammar)
    parser.setup()
    
    assert parser.stack == [(grammar.dfas[grammar.start], 0, (grammar.start, None, None, []))]
    assert parser.rootnode is None
    assert parser.used_names == set()
