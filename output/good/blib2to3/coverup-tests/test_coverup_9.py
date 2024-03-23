# file src/blib2to3/pgen2/grammar.py:129-147
# lines [129, 133, 134, 142, 143, 144, 145, 146, 147]
# branches ['134->142', '134->143']

import pytest
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar_instance():
    grammar = Grammar()
    grammar.symbol2number = {'symbol': 1}
    grammar.number2symbol = {1: 'symbol'}
    grammar.dfas = {'dfa': 'definition'}
    grammar.keywords = {'keyword': 'definition'}
    grammar.tokens = {'token': 'definition'}
    grammar.symbol2label = {'symbol': 'label'}
    grammar.labels = ['label1', 'label2']
    grammar.states = ['state1', 'state2']
    grammar.start = 'start_symbol'
    grammar.async_keywords = True
    return grammar

def test_grammar_copy(grammar_instance):
    copied_grammar = grammar_instance.copy()
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
    # Ensure that the dictionaries are copies and not the same object
    assert copied_grammar.symbol2number is not grammar_instance.symbol2number
    assert copied_grammar.number2symbol is not grammar_instance.number2symbol
    assert copied_grammar.dfas is not grammar_instance.dfas
    assert copied_grammar.keywords is not grammar_instance.keywords
    assert copied_grammar.tokens is not grammar_instance.tokens
    assert copied_grammar.symbol2label is not grammar_instance.symbol2label
    # Ensure that the lists are copies and not the same object
    assert copied_grammar.labels is not grammar_instance.labels
    assert copied_grammar.states is not grammar_instance.states
