# file src/blib2to3/pgen2/grammar.py:129-147
# lines [129, 133, 134, 142, 143, 144, 145, 146, 147]
# branches ['134->142', '134->143']

import pytest
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def mock_grammar():
    class MockGrammar(Grammar):
        def __init__(self):
            self.symbol2number = {'a': 1}
            self.number2symbol = {1: 'a'}
            self.dfas = {'a': (1,)}
            self.keywords = {'if': 1}
            self.tokens = {'NAME': 1}
            self.symbol2label = {'a': 'label'}
            self.labels = ['label1']
            self.states = ['state1']
            self.start = 'start'
            self.async_keywords = False

    return MockGrammar()

def test_grammar_copy(mock_grammar):
    copied_grammar = mock_grammar.copy()

    assert copied_grammar is not mock_grammar
    assert copied_grammar.symbol2number == mock_grammar.symbol2number
    assert copied_grammar.number2symbol == mock_grammar.number2symbol
    assert copied_grammar.dfas == mock_grammar.dfas
    assert copied_grammar.keywords == mock_grammar.keywords
    assert copied_grammar.tokens == mock_grammar.tokens
    assert copied_grammar.symbol2label == mock_grammar.symbol2label
    assert copied_grammar.labels == mock_grammar.labels
    assert copied_grammar.states == mock_grammar.states
    assert copied_grammar.start == mock_grammar.start
    assert copied_grammar.async_keywords == mock_grammar.async_keywords
