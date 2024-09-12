# file: src/blib2to3/pgen2/pgen.py:90-134
# asked: {"lines": [116, 117, 118, 120, 121, 123, 124, 125, 128, 129, 130, 132, 133, 134], "branches": [[93, 116], [118, 120], [118, 128], [120, 121], [120, 123], [129, 130], [129, 132]]}
# gained: {"lines": [116, 117, 118, 120, 121, 123, 124, 125, 128, 129, 130, 132, 133, 134], "branches": [[93, 116], [118, 120], [118, 128], [120, 121], [120, 123], [129, 130], [129, 132]]}

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
def parser_generator(mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.parse', return_value=({}, 'file_input'))
    stream = StringIO("")
    return ParserGenerator("filename", stream)

def test_make_label_keyword(grammar, parser_generator):
    label = "'keyword'"
    ilabel = parser_generator.make_label(grammar, label)
    assert grammar.labels == [(token.NAME, 'keyword')]
    assert grammar.keywords['keyword'] == ilabel

def test_make_label_operator(grammar, parser_generator):
    label = "'+'"
    ilabel = parser_generator.make_label(grammar, label)
    assert grammar.labels == [(token.PLUS, None)]
    assert grammar.tokens[token.PLUS] == ilabel

def test_make_label_existing_keyword(grammar, parser_generator):
    label = "'keyword'"
    grammar.keywords['keyword'] = 42
    ilabel = parser_generator.make_label(grammar, label)
    assert ilabel == 42

def test_make_label_existing_operator(grammar, parser_generator):
    label = "'+'"
    grammar.tokens[token.PLUS] = 42
    ilabel = parser_generator.make_label(grammar, label)
    assert ilabel == 42
