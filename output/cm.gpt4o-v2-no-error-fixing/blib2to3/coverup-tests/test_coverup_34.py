# file: src/blib2to3/pgen2/parse.py:87-117
# asked: {"lines": [87, 116, 117], "branches": []}
# gained: {"lines": [87, 116, 117], "branches": []}

import pytest
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar

def test_parser_init_with_convert():
    def dummy_convert(grammar, node):
        return node

    grammar = Grammar()
    parser = Parser(grammar, convert=dummy_convert)
    
    assert parser.grammar is grammar
    assert parser.convert is dummy_convert

def test_parser_init_without_convert():
    grammar = Grammar()
    parser = Parser(grammar)
    
    assert parser.grammar is grammar
    assert callable(parser.convert)
