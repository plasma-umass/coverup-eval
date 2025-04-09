# file: src/blib2to3/pgen2/pgen.py:29-30
# asked: {"lines": [29, 30], "branches": []}
# gained: {"lines": [29, 30], "branches": []}

import pytest
from blib2to3.pgen2 import pgen, grammar

@pytest.fixture
def pgen_grammar():
    return pgen.PgenGrammar()

def test_pgen_grammar_initialization(pgen_grammar):
    assert isinstance(pgen_grammar, grammar.Grammar)
    assert pgen_grammar.symbol2number == {}
    assert pgen_grammar.number2symbol == {}
    assert pgen_grammar.states == []
    assert pgen_grammar.dfas == {}
    assert pgen_grammar.labels == [(0, 'EMPTY')]
    assert pgen_grammar.keywords == {}
    assert pgen_grammar.tokens == {}
    assert pgen_grammar.symbol2label == {}
    assert pgen_grammar.start == 256
    assert pgen_grammar.async_keywords is False
