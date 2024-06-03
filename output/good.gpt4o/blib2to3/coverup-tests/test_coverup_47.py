# file src/blib2to3/pgen2/parse.py:87-117
# lines [87, 116, 117]
# branches []

import pytest
from blib2to3.pgen2.parse import Parser
from blib2to3.pgen2.grammar import Grammar

def test_parser_initialization():
    # Mock Grammar instance
    mock_grammar = Grammar()

    # Test without convert function
    parser = Parser(mock_grammar)
    assert parser.grammar is mock_grammar
    assert parser.convert is not None  # Should be lam_sub by default

    # Test with a custom convert function
    def custom_convert(grammar, node):
        return node

    parser_with_convert = Parser(mock_grammar, convert=custom_convert)
    assert parser_with_convert.grammar is mock_grammar
    assert parser_with_convert.convert is custom_convert
