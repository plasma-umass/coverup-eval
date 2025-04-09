# file: src/blib2to3/pgen2/grammar.py:129-147
# asked: {"lines": [129, 133, 134, 142, 143, 144, 145, 146, 147], "branches": [[134, 142], [134, 143]]}
# gained: {"lines": [129, 133, 134, 142, 143, 144, 145, 146, 147], "branches": [[134, 142], [134, 143]]}

import pytest
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar_instance():
    grammar = Grammar()
    grammar.symbol2number = {'a': 1}
    grammar.number2symbol = {1: 'a'}
    grammar.dfas = {'a': [(1, 2)]}
    grammar.keywords = {'if': 1}
    grammar.tokens = {'NAME': 1}
    grammar.symbol2label = {'a': 'label'}
    grammar.labels = ['label1']
    grammar.states = ['state1']
    grammar.start = 'start'
    grammar.async_keywords = False
    return grammar

def test_grammar_copy(grammar_instance):
    copied_grammar = grammar_instance.copy()
    
    assert copied_grammar is not grammar_instance
    assert copied_grammar.symbol2number == grammar_instance.symbol2number
    assert copied_grammar.number2symbol == grammar_instance.number2symbol
    assert copied_grammar.dfas == grammar_instance.dfas
    assert copied_grammar.keywords == grammar_instance.keywords
    assert copied_grammar.tokens == grammar_instance.tokens
    assert copied_grammar.symbol2label == grammar_instance.symbol2label
    assert copied_grammar.labels == grammar_instance.labels
    assert copied_grammar.states == grammar_instance.states
    assert copied_grammar.start == grammar_instance.start
    assert copied_grammar.async_keywords == grammar_instance.async_keywords
