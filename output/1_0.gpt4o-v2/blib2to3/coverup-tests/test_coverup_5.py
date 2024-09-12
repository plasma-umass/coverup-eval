# file: src/blib2to3/pygram.py:136-143
# asked: {"lines": [136, 137, 138, 139, 140, 141, 142, 143], "branches": []}
# gained: {"lines": [136, 137, 138, 139, 140, 141, 142, 143], "branches": []}

import pytest
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pygram import _pattern_symbols

@pytest.fixture
def mock_grammar():
    class MockGrammar:
        symbol2number = {
            'Alternative': 256,
            'Alternatives': 257,
            'Details': 258,
            'Matcher': 259,
            'NegatedUnit': 260,
            'Repeater': 261,
            'Unit': 262
        }
    return MockGrammar()

def test_pattern_symbols_initialization(mock_grammar):
    pattern_symbols = _pattern_symbols(mock_grammar)
    
    assert pattern_symbols.Alternative == 256
    assert pattern_symbols.Alternatives == 257
    assert pattern_symbols.Details == 258
    assert pattern_symbols.Matcher == 259
    assert pattern_symbols.NegatedUnit == 260
    assert pattern_symbols.Repeater == 261
    assert pattern_symbols.Unit == 262
