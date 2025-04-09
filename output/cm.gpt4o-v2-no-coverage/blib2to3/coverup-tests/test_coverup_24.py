# file: src/blib2to3/pgen2/parse.py:119-141
# asked: {"lines": [119, 132, 133, 137, 138, 139, 140, 141], "branches": [[132, 133], [132, 137]]}
# gained: {"lines": [119, 132, 133, 137, 138, 139, 140, 141], "branches": [[132, 133], [132, 137]]}

import pytest
from unittest.mock import Mock
from blib2to3.pytree import NL, RawNode
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar
from typing import Optional, Tuple, List, Set

DFAS = Tuple[Mock, dict]

class MockGrammar(Grammar):
    def __init__(self, start, dfas):
        self.start = start
        self.dfas = dfas

@pytest.fixture
def parser():
    grammar = MockGrammar(start=1, dfas={1: Mock()})
    parser = Parser(grammar)
    return parser

def test_setup_with_default_start(parser):
    parser.setup()
    assert parser.stack == [(parser.grammar.dfas[1], 0, (1, None, None, []))]
    assert parser.rootnode is None
    assert parser.used_names == set()

def test_setup_with_custom_start(parser):
    parser.grammar.dfas[2] = Mock()
    parser.setup(start=2)
    assert parser.stack == [(parser.grammar.dfas[2], 0, (2, None, None, []))]
    assert parser.rootnode is None
    assert parser.used_names == set()
