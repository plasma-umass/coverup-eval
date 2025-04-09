# file: src/blib2to3/pgen2/pgen.py:428-430
# asked: {"lines": [428, 429, 430], "branches": []}
# gained: {"lines": [428, 429, 430], "branches": []}

import pytest
from pathlib import Path
from blib2to3.pgen2.pgen import generate_grammar, ParserGenerator, PgenGrammar

@pytest.fixture
def mock_parser_generator(mocker):
    mock = mocker.patch('blib2to3.pgen2.pgen.ParserGenerator')
    instance = mock.return_value
    instance.make_grammar.return_value = PgenGrammar()
    return mock

def test_generate_grammar_with_default_filename(mock_parser_generator):
    grammar = generate_grammar()
    mock_parser_generator.assert_called_once_with("Grammar.txt")
    assert isinstance(grammar, PgenGrammar)

def test_generate_grammar_with_custom_filename(mock_parser_generator):
    custom_filename = Path("CustomGrammar.txt")
    grammar = generate_grammar(custom_filename)
    mock_parser_generator.assert_called_once_with(custom_filename)
    assert isinstance(grammar, PgenGrammar)
