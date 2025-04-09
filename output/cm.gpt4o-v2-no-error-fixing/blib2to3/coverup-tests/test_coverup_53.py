# file: src/blib2to3/pgen2/pgen.py:40-53
# asked: {"lines": [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": [[42, 43], [42, 45], [50, 51], [50, 52]]}
# gained: {"lines": [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": [[42, 43], [42, 45], [50, 51], [50, 52]]}

import pytest
from unittest.mock import mock_open, patch
from blib2to3.pgen2.pgen import ParserGenerator
from pathlib import Path

@pytest.fixture
def mock_parse(mocker):
    return mocker.patch.object(ParserGenerator, 'parse', return_value=({}, 'start'))

@pytest.fixture
def mock_gettoken(mocker):
    return mocker.patch.object(ParserGenerator, 'gettoken')

@pytest.fixture
def mock_addfirstsets(mocker):
    return mocker.patch.object(ParserGenerator, 'addfirstsets')

def test_parser_generator_with_stream(mock_parse, mock_gettoken, mock_addfirstsets):
    mock_stream = mock_open(read_data="some data")
    with patch("builtins.open", mock_stream):
        stream = open("dummy")
        pg = ParserGenerator(Path("dummy"), stream)
        assert pg.stream == stream
        assert pg.filename == Path("dummy")
        assert mock_parse.called
        assert mock_gettoken.called
        assert mock_addfirstsets.called

def test_parser_generator_without_stream(mock_parse, mock_gettoken, mock_addfirstsets):
    mock_stream = mock_open(read_data="some data")
    with patch("builtins.open", mock_stream):
        pg = ParserGenerator(Path("dummy"))
        assert pg.stream is not None
        assert pg.filename == Path("dummy")
        assert mock_parse.called
        assert mock_gettoken.called
        assert mock_addfirstsets.called
