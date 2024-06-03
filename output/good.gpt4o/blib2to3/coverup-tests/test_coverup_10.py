# file src/blib2to3/pgen2/pgen.py:40-53
# lines [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
# branches ['42->43', '42->45', '50->51', '50->52']

import pytest
from unittest import mock
from pathlib import Path
from blib2to3.pgen2.pgen import ParserGenerator

@pytest.fixture
def mock_open(mocker):
    mock_file = mocker.mock_open(read_data="def test(): pass\n")
    mocker.patch("builtins.open", mock_file)
    return mock_file

def test_parser_generator_with_stream(mock_open):
    filename = Path("dummy_file.py")
    stream = open(filename)
    with mock.patch.object(ParserGenerator, 'parse', return_value=({}, 'start')):
        parser_generator = ParserGenerator(filename, stream)
    
    assert parser_generator.filename == filename
    assert parser_generator.stream == stream
    assert parser_generator.first == {}

def test_parser_generator_without_stream(mock_open):
    filename = Path("dummy_file.py")
    with mock.patch.object(ParserGenerator, 'parse', return_value=({}, 'start')):
        parser_generator = ParserGenerator(filename)
    
    assert parser_generator.filename == filename
    assert parser_generator.stream is not None
    assert parser_generator.first == {}
    mock_open().close.assert_called_once()
