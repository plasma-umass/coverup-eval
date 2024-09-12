# file: src/blib2to3/pgen2/pgen.py:40-53
# asked: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": [[42, 43], [42, 45], [50, 51], [50, 52]]}
# gained: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": [[42, 43], [42, 45], [50, 51], [50, 52]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator
from blib2to3.pgen2 import token
from pathlib import Path
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_file():
    m = mock_open(read_data="test : pass\n")
    with patch("builtins.open", m):
        yield m

def test_parser_generator_with_stream(mock_file):
    filename = Path("test_file.py")
    stream = open(filename)
    with patch.object(ParserGenerator, 'parse', return_value=({}, 'test')):
        with patch.object(ParserGenerator, 'addfirstsets'):
            pg = ParserGenerator(filename, stream)
            assert pg.filename == filename
            assert pg.stream == stream
            assert isinstance(pg.dfas, dict)
            assert isinstance(pg.startsymbol, str)
            assert isinstance(pg.first, dict)

def test_parser_generator_without_stream(mock_file):
    filename = Path("test_file.py")
    with patch.object(ParserGenerator, 'parse', return_value=({}, 'test')):
        with patch.object(ParserGenerator, 'addfirstsets'):
            pg = ParserGenerator(filename)
            assert pg.filename == filename
            assert pg.stream is not None
            assert isinstance(pg.dfas, dict)
            assert isinstance(pg.startsymbol, str)
            assert isinstance(pg.first, dict)
