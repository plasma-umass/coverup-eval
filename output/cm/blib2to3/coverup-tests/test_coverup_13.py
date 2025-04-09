# file src/blib2to3/pgen2/pgen.py:90-134
# lines [90, 92, 93, 95, 97, 98, 100, 101, 102, 105, 106, 107, 108, 109, 111, 112, 113, 116, 117, 118, 120, 121, 123, 124, 125, 128, 129, 130, 132, 133, 134]
# branches ['93->95', '93->116', '95->97', '95->105', '97->98', '97->100', '108->109', '108->111', '118->120', '118->128', '120->121', '120->123', '129->130', '129->132']

import pytest
from blib2to3.pgen2 import pgen
from blib2to3.pgen2 import grammar
import token

class MockPgenGrammar:
    def __init__(self):
        self.labels = []
        self.symbol2number = {}
        self.symbol2label = {}
        self.tokens = {}
        self.keywords = {}

@pytest.fixture
def mock_pgen_grammar():
    return MockPgenGrammar()

def test_make_label_with_symbol_name(mock_pgen_grammar, mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.__init__', return_value=None)
    parser_gen = pgen.ParserGenerator()
    mock_pgen_grammar.symbol2number['symbol'] = 1
    label = parser_gen.make_label(mock_pgen_grammar, 'symbol')
    assert label == 0
    assert mock_pgen_grammar.labels == [(1, None)]
    assert mock_pgen_grammar.symbol2label == {'symbol': 0}

def test_make_label_with_named_token(mock_pgen_grammar, mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.__init__', return_value=None)
    parser_gen = pgen.ParserGenerator()
    label = parser_gen.make_label(mock_pgen_grammar, 'NAME')
    itoken = getattr(token, 'NAME', None)
    assert label == 0
    assert mock_pgen_grammar.labels == [(itoken, None)]
    assert mock_pgen_grammar.tokens == {itoken: 0}

def test_make_label_with_keyword(mock_pgen_grammar, mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.__init__', return_value=None)
    parser_gen = pgen.ParserGenerator()
    label = parser_gen.make_label(mock_pgen_grammar, "'if'")
    assert label == 0
    assert mock_pgen_grammar.labels == [(token.NAME, 'if')]
    assert mock_pgen_grammar.keywords == {'if': 0}

def test_make_label_with_operator(mock_pgen_grammar, mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.__init__', return_value=None)
    parser_gen = pgen.ParserGenerator()
    label = parser_gen.make_label(mock_pgen_grammar, "'+'")
    itoken = grammar.opmap['+']
    assert label == 0
    assert mock_pgen_grammar.labels == [(itoken, None)]
    assert mock_pgen_grammar.tokens == {itoken: 0}
