# file: src/blib2to3/pgen2/grammar.py:129-147
# asked: {"lines": [129, 133, 134, 142, 143, 144, 145, 146, 147], "branches": [[134, 142], [134, 143]]}
# gained: {"lines": [129, 133, 134, 142, 143, 144, 145, 146, 147], "branches": [[134, 142], [134, 143]]}

import pytest
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar():
    g = Grammar()
    g.symbol2number = {"stmt": 256}
    g.number2symbol = {256: "stmt"}
    g.dfas = {256: [[], {1: 1}]}
    g.keywords = {"if": 1}
    g.tokens = {1: 256}
    g.symbol2label = {"stmt": 1}
    g.labels = [(256, "stmt")]
    g.states = [[(1, 1)]]
    g.start = 256
    g.async_keywords = True
    return g

def test_grammar_copy(grammar):
    new_grammar = grammar.copy()
    
    assert new_grammar is not grammar
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
