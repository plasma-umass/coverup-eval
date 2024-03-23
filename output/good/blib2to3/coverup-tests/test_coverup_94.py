# file src/blib2to3/pgen2/pgen.py:40-53
# lines [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
# branches ['42->43', '42->45', '50->51', '50->52']

import pytest
from pathlib import Path
from blib2to3.pgen2 import tokenize
from blib2to3.pgen2.pgen import ParserGenerator

@pytest.fixture
def mock_open(mocker):
    # Create a minimal grammar that can be parsed without error
    grammar_data = "start: symbol\nsymbol: 'TOKEN'\n"
    mock_file = mocker.mock_open(read_data=grammar_data)
    mocker.patch("builtins.open", mock_file)
    return mock_file

def test_parser_generator_init_with_stream_none(mock_open, tmp_path):
    # Create a temporary file to simulate the filename input
    temp_file = tmp_path / "temp_grammar_file.txt"
    # Write a minimal grammar to the temp file to avoid SyntaxError
    temp_file.write_text("start: symbol\nsymbol: 'TOKEN'\n")

    # Call the ParserGenerator with stream=None, which should trigger the open call
    parser_gen = ParserGenerator(filename=temp_file, stream=None)

    # Assertions to check if the file was opened and the ParserGenerator was initialized correctly
    mock_open.assert_called_once_with(temp_file)
    assert parser_gen.filename == temp_file
    assert parser_gen.stream is not None
    assert hasattr(parser_gen, 'dfas')
    assert hasattr(parser_gen, 'startsymbol')
    assert hasattr(parser_gen, 'first')
    assert callable(parser_gen.stream.close)

    # Clean up by closing the stream if it was not closed
    if not parser_gen.stream.closed:
        parser_gen.stream.close()
