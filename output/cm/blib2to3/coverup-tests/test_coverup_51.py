# file src/blib2to3/pgen2/parse.py:87-117
# lines [87, 116, 117]
# branches []

import pytest
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar():
    return Grammar()

@pytest.fixture
def convert_function():
    def convert(grammar, node):
        return node
    return convert

def test_parser_init_with_convert_function(grammar, convert_function):
    parser = Parser(grammar, convert_function)
    assert parser.grammar == grammar
    assert parser.convert == convert_function

def test_parser_init_without_convert_function(grammar):
    parser = Parser(grammar)
    assert parser.grammar == grammar
    assert parser.convert.__name__ == 'lam_sub'  # Assuming lam_sub is a known function in the module
