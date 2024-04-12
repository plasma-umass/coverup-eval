# file src/blib2to3/pgen2/grammar.py:85-96
# lines [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96]
# branches []

import pytest
from blib2to3.pgen2.grammar import Grammar

def test_grammar_init():
    grammar = Grammar()
    assert isinstance(grammar.symbol2number, dict)
    assert isinstance(grammar.number2symbol, dict)
    assert isinstance(grammar.states, list)
    assert isinstance(grammar.dfas, dict)
    assert isinstance(grammar.labels, list)
    assert grammar.labels == [(0, "EMPTY")]
    assert isinstance(grammar.keywords, dict)
    assert isinstance(grammar.tokens, dict)
    assert isinstance(grammar.symbol2label, dict)
    assert grammar.start == 256
    assert grammar.async_keywords is False
