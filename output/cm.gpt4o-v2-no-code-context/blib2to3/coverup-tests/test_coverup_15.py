# file: src/blib2to3/pgen2/pgen.py:40-53
# asked: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": [[42, 43], [42, 45], [50, 51], [50, 52]]}
# gained: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": [[42, 43], [42, 45], [50, 51], [50, 52]]}

import pytest
from unittest.mock import mock_open, patch, MagicMock
from pathlib import Path
from blib2to3.pgen2.pgen import ParserGenerator

@pytest.fixture
def mock_tokenize(mocker):
    mocker.patch('blib2to3.pgen2.pgen.tokenize.generate_tokens', return_value=iter([('NAME', 'data', (1, 0), (1, 4), 'data')]))

@pytest.fixture
def mock_parse(mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.parse', return_value=({}, None))

def test_parser_generator_with_stream(mock_tokenize, mock_parse):
    mock_stream = mock_open(read_data="data")
    with patch('builtins.open', mock_stream):
        stream = open('dummy')
        pg = ParserGenerator(Path('dummy'), stream)
        assert pg.filename == Path('dummy')
        assert pg.stream == stream
        assert pg.dfas == {}
        assert pg.startsymbol is None
        assert pg.first == {}

def test_parser_generator_without_stream(mock_tokenize, mock_parse):
    mock_stream = mock_open(read_data="data")
    with patch('builtins.open', mock_stream):
        pg = ParserGenerator(Path('dummy'))
        assert pg.filename == Path('dummy')
        assert pg.dfas == {}
        assert pg.startsymbol is None
        assert pg.first == {}
