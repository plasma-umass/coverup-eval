# file src/blib2to3/pgen2/parse.py:119-141
# lines [119, 132, 133, 137, 138, 139, 140, 141]
# branches ['132->133', '132->137']

import pytest
from unittest.mock import Mock
from blib2to3.pgen2.parse import Parser

@pytest.fixture
def mock_grammar():
    mock_grammar = Mock()
    mock_grammar.start = 1
    mock_grammar.dfas = {1: 'dfa1', 2: 'dfa2'}
    return mock_grammar

def test_parser_setup_with_default_start(mock_grammar):
    parser = Parser(mock_grammar)
    parser.setup()
    
    assert parser.stack == [('dfa1', 0, (1, None, None, []))]
    assert parser.rootnode is None
    assert parser.used_names == set()

def test_parser_setup_with_custom_start(mock_grammar):
    parser = Parser(mock_grammar)
    parser.setup(start=2)
    
    assert parser.stack == [('dfa2', 0, (2, None, None, []))]
    assert parser.rootnode is None
    assert parser.used_names == set()
