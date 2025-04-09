# file: src/blib2to3/pgen2/grammar.py:129-147
# asked: {"lines": [129, 133, 134, 142, 143, 144, 145, 146, 147], "branches": [[134, 142], [134, 143]]}
# gained: {"lines": [129, 133, 134, 142, 143, 144, 145, 146, 147], "branches": [[134, 142], [134, 143]]}

import pytest
from blib2to3.pgen2.grammar import Grammar

def test_grammar_copy():
    # Create a Grammar instance and set attributes
    grammar = Grammar()
    grammar.symbol2number = {'a': 1, 'b': 2}
    grammar.number2symbol = {1: 'a', 2: 'b'}
    grammar.dfas = {'a': [(1, 2)], 'b': [(2, 3)]}
    grammar.keywords = {'if': 1, 'else': 2}
    grammar.tokens = {'NAME': 1, 'NUMBER': 2}
    grammar.symbol2label = {'a': 'label_a', 'b': 'label_b'}
    grammar.labels = ['label1', 'label2']
    grammar.states = ['state1', 'state2']
    grammar.start = 'start_symbol'
    grammar.async_keywords = {'await': 1, 'async': 2}

    # Copy the grammar
    new_grammar = grammar.copy()

    # Assertions to verify the copy
    assert new_grammar is not grammar
    assert new_grammar.__class__ is grammar.__class__
    assert new_grammar.symbol2number == grammar.symbol2number
    assert new_grammar.number2symbol == grammar.number2symbol
    assert new_grammar.dfas == grammar.dfas
    assert new_grammar.keywords == grammar.keywords
    assert new_grammar.tokens == grammar.tokens
    assert new_grammar.symbol2label == grammar.symbol2label
    assert new_grammar.labels == grammar.labels
    assert new_grammar.states == grammar.states
    assert new_grammar.start == grammar.start
    assert new_grammar.async_keywords == grammar.async_keywords
