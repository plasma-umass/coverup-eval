# file: src/blib2to3/pgen2/pgen.py:80-88
# asked: {"lines": [80, 81, 82, 83, 84, 85, 87, 88], "branches": [[84, 85], [84, 88]]}
# gained: {"lines": [80, 81, 82, 83, 84, 85, 87, 88], "branches": [[84, 85], [84, 88]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, PgenGrammar
from blib2to3.pgen2 import token

@pytest.fixture
def parser_generator():
    # Create a mock ParserGenerator object with necessary attributes
    pg = ParserGenerator.__new__(ParserGenerator)
    pg.first = {
        'test': {'NAME': 1, 'NUMBER': 1}
    }
    return pg

@pytest.fixture
def pgen_grammar():
    # Create a mock PgenGrammar object with necessary attributes
    g = PgenGrammar()
    g.labels = []
    g.symbol2number = {'NAME': 1, 'NUMBER': 2}
    g.symbol2label = {}
    g.tokens = {}
    g.keywords = {}
    return g

def test_make_first(parser_generator, pgen_grammar):
    result = parser_generator.make_first(pgen_grammar, 'test')
    assert result == {parser_generator.make_label(pgen_grammar, 'NAME'): 1,
                      parser_generator.make_label(pgen_grammar, 'NUMBER'): 1}

def test_make_first_empty(parser_generator, pgen_grammar):
    parser_generator.first['empty'] = {}
    result = parser_generator.make_first(pgen_grammar, 'empty')
    assert result == {}

def test_make_first_assertion_error(parser_generator, pgen_grammar):
    parser_generator.first['none'] = None
    with pytest.raises(AssertionError):
        parser_generator.make_first(pgen_grammar, 'none')
