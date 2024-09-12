# file: src/blib2to3/pgen2/grammar.py:129-147
# asked: {"lines": [129, 133, 134, 142, 143, 144, 145, 146, 147], "branches": [[134, 142], [134, 143]]}
# gained: {"lines": [129, 133, 134, 142, 143, 144, 145, 146, 147], "branches": [[134, 142], [134, 143]]}

import pytest
from blib2to3.pgen2.grammar import Grammar

def test_grammar_copy():
    grammar = Grammar()
    grammar.symbol2number = {'a': 1}
    grammar.number2symbol = {1: 'a'}
    grammar.dfas = {1: ([], {})}
    grammar.keywords = {'if': 1}
    grammar.tokens = {1: 1}
    grammar.symbol2label = {'a': 1}
    grammar.labels = [(1, 'a')]
    grammar.states = [[(1, 2)]]
    grammar.start = 1
    grammar.async_keywords = True

    grammar_copy = grammar.copy()

    assert grammar_copy.symbol2number == grammar.symbol2number
    assert grammar_copy.number2symbol == grammar.number2symbol
    assert grammar_copy.dfas == grammar.dfas
    assert grammar_copy.keywords == grammar.keywords
    assert grammar_copy.tokens == grammar.tokens
    assert grammar_copy.symbol2label == grammar.symbol2label
    assert grammar_copy.labels == grammar.labels
    assert grammar_copy.states == grammar.states
    assert grammar_copy.start == grammar.start
    assert grammar_copy.async_keywords == grammar.async_keywords
    assert grammar_copy is not grammar
