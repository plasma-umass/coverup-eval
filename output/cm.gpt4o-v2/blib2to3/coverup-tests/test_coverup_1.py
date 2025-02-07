# file: src/blib2to3/pgen2/grammar.py:85-96
# asked: {"lines": [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96], "branches": []}
# gained: {"lines": [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96], "branches": []}

import pytest
from blib2to3.pgen2.grammar import Grammar

def test_grammar_initialization():
    grammar = Grammar()
    
    assert grammar.symbol2number == {}
    assert grammar.number2symbol == {}
    assert grammar.states == []
    assert grammar.dfas == {}
    assert grammar.labels == [(0, 'EMPTY')]
    assert grammar.keywords == {}
    assert grammar.tokens == {}
    assert grammar.symbol2label == {}
    assert grammar.start == 256
    assert grammar.async_keywords == False
