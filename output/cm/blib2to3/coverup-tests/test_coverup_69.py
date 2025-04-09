# file src/blib2to3/pgen2/pgen.py:428-430
# lines [428, 429, 430]
# branches []

import pytest
from pathlib import Path
from blib2to3.pgen2.pgen import generate_grammar
from blib2to3.pgen2.grammar import Grammar

def test_generate_grammar(tmp_path, mocker):
    # Create a temporary Grammar.txt file
    grammar_file = tmp_path / "Grammar.txt"
    grammar_file.write_text("# Dummy grammar content")

    # Mock the ParserGenerator to return a Grammar without actual parsing
    mock_grammar = Grammar()
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator', return_value=mocker.Mock(make_grammar=mocker.Mock(return_value=mock_grammar)))

    # Call the function under test
    generated_grammar = generate_grammar(grammar_file)

    # Assert that the returned object is a Grammar
    assert isinstance(generated_grammar, Grammar)

    # Clean up the temporary file
    grammar_file.unlink()
