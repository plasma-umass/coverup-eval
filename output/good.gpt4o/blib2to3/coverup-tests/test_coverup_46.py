# file src/blib2to3/pgen2/pgen.py:428-430
# lines [428, 429, 430]
# branches []

import pytest
from pathlib import Path
from blib2to3.pgen2.pgen import generate_grammar, PgenGrammar

def test_generate_grammar(mocker):
    # Mock the ParserGenerator class and its methods
    mock_parser_generator = mocker.patch('blib2to3.pgen2.pgen.ParserGenerator')
    mock_make_grammar = mock_parser_generator.return_value.make_grammar
    mock_make_grammar.return_value = PgenGrammar()

    # Call the function with a test filename
    test_filename = Path("test_grammar.txt")
    result = generate_grammar(test_filename)

    # Assertions to verify the correct behavior
    mock_parser_generator.assert_called_once_with(test_filename)
    mock_make_grammar.assert_called_once()
    assert isinstance(result, PgenGrammar)
