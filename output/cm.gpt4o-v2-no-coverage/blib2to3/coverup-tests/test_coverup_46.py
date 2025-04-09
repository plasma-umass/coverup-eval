# file: src/blib2to3/pgen2/pgen.py:90-134
# asked: {"lines": [90, 92, 93, 95, 97, 98, 100, 101, 102, 105, 106, 107, 108, 109, 111, 112, 113, 116, 117, 118, 120, 121, 123, 124, 125, 128, 129, 130, 132, 133, 134], "branches": [[93, 95], [93, 116], [95, 97], [95, 105], [97, 98], [97, 100], [108, 109], [108, 111], [118, 120], [118, 128], [120, 121], [120, 123], [129, 130], [129, 132]]}
# gained: {"lines": [90, 92, 93, 95, 97, 98, 100, 101, 102, 105, 106, 107, 108, 109, 111, 112, 113, 116, 117, 118, 120, 121, 123, 124, 125, 128, 129, 130, 132, 133, 134], "branches": [[93, 95], [93, 116], [95, 97], [95, 105], [97, 98], [97, 100], [108, 109], [108, 111], [118, 120], [118, 128], [120, 121], [120, 123], [129, 130], [129, 132]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pgen2 import token
from io import StringIO

@pytest.fixture
def grammar():
    g = Grammar()
    g.labels = []
    g.symbol2number = {}
    g.symbol2label = {}
    g.tokens = {}
    g.keywords = {}
    return g

@pytest.fixture
def parser_generator():
    stream = StringIO("symbol: NAME\n")
    return ParserGenerator("filename", stream)

def test_make_label_symbol(parser_generator, grammar):
    grammar.symbol2number['symbol'] = 1
    label = 'symbol'
    result = parser_generator.make_label(grammar, label)
    assert result == 0
    assert grammar.labels == [(1, None)]
    assert grammar.symbol2label['symbol'] == 0

def test_make_label_named_token(parser_generator, grammar):
    label = 'NAME'
    result = parser_generator.make_label(grammar, label)
    assert result == 0
    assert grammar.labels == [(token.NAME, None)]
    assert grammar.tokens[token.NAME] == 0

def test_make_label_keyword(parser_generator, grammar):
    label = '"keyword"'
    result = parser_generator.make_label(grammar, label)
    assert result == 0
    assert grammar.labels == [(token.NAME, 'keyword')]
    assert grammar.keywords['keyword'] == 0

def test_make_label_operator(parser_generator, grammar):
    label = '"+"'
    result = parser_generator.make_label(grammar, label)
    assert result == 0
    assert grammar.labels == [(token.PLUS, None)]
    assert grammar.tokens[token.PLUS] == 0

def test_make_label_existing_symbol(parser_generator, grammar):
    grammar.symbol2number['symbol'] = 1
    grammar.symbol2label['symbol'] = 0
    label = 'symbol'
    result = parser_generator.make_label(grammar, label)
    assert result == 0

def test_make_label_existing_named_token(parser_generator, grammar):
    label = 'NAME'
    grammar.tokens[token.NAME] = 0
    result = parser_generator.make_label(grammar, label)
    assert result == 0

def test_make_label_existing_keyword(parser_generator, grammar):
    label = '"keyword"'
    grammar.keywords['keyword'] = 0
    result = parser_generator.make_label(grammar, label)
    assert result == 0

def test_make_label_existing_operator(parser_generator, grammar):
    label = '"+"'
    grammar.tokens[token.PLUS] = 0
    result = parser_generator.make_label(grammar, label)
    assert result == 0
