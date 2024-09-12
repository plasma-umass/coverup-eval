# file: src/blib2to3/pygram.py:24-32
# asked: {"lines": [24, 25, 31, 32], "branches": [[31, 0], [31, 32]]}
# gained: {"lines": [24, 25, 31, 32], "branches": [[31, 0], [31, 32]]}

import pytest
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pygram import Symbols

def test_symbols_init():
    # Create a mock Grammar object
    grammar = Grammar()
    grammar.symbol2number = {
        'symbol1': 256,
        'symbol2': 257,
        'symbol3': 258
    }

    # Initialize Symbols with the mock Grammar
    symbols = Symbols(grammar)

    # Assert that the attributes are set correctly
    assert symbols.symbol1 == 256
    assert symbols.symbol2 == 257
    assert symbols.symbol3 == 258

    # Clean up
    del symbols
    del grammar
