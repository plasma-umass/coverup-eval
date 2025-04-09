# file src/blib2to3/pgen2/pgen.py:90-134
# lines [90, 92, 93, 95, 97, 98, 100, 101, 102, 105, 106, 107, 108, 109, 111, 112, 113, 116, 117, 118, 120, 121, 123, 124, 125, 128, 129, 130, 132, 133, 134]
# branches ['93->95', '93->116', '95->97', '95->105', '97->98', '97->100', '108->109', '108->111', '118->120', '118->128', '120->121', '120->123', '129->130', '129->132']

import pytest
from blib2to3.pgen2.pgen import ParserGenerator
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pgen2 import token, grammar

@pytest.fixture
def mock_grammar(mocker):
    g = Grammar()
    g.symbol2number = {'symbol': 1}
    g.symbol2label = {}
    g.tokens = {}
    g.keywords = {}
    g.labels = []
    return g

@pytest.fixture
def parser_generator(mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.__init__', lambda x, y: None)
    return ParserGenerator('dummy')

def test_make_label_symbol(mock_grammar, parser_generator):
    label = 'symbol'
    result = parser_generator.make_label(mock_grammar, label)
    assert result == 0
    assert mock_grammar.symbol2label[label] == 0
    assert mock_grammar.labels == [(1, None)]

def test_make_label_named_token(mock_grammar, parser_generator, mocker):
    label = 'NAME'
    mocker.patch.object(token, 'NAME', 1)
    mocker.patch.object(token, 'tok_name', {1: 'NAME'})
    result = parser_generator.make_label(mock_grammar, label)
    assert result == 0
    assert mock_grammar.tokens[1] == 0
    assert mock_grammar.labels == [(1, None)]

def test_make_label_keyword(mock_grammar, parser_generator):
    label = '"keyword"'
    result = parser_generator.make_label(mock_grammar, label)
    assert result == 0
    assert mock_grammar.keywords['keyword'] == 0
    assert mock_grammar.labels == [(token.NAME, 'keyword')]

def test_make_label_operator(mock_grammar, parser_generator, mocker):
    label = '"+"'
    mocker.patch.object(grammar, 'opmap', {'+': 1})
    result = parser_generator.make_label(mock_grammar, label)
    assert result == 0
    assert mock_grammar.tokens[1] == 0
    assert mock_grammar.labels == [(1, None)]
