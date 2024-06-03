# file src/blib2to3/pgen2/pgen.py:33-39
# lines [33, 35, 36, 37, 38]
# branches []

import pytest
from unittest.mock import MagicMock, patch
from blib2to3.pgen2.pgen import ParserGenerator

@patch('blib2to3.pgen2.pgen.ParserGenerator.parse', return_value=({}, 'start'))
def test_parser_generator_initialization(mock_parse):
    mock_path = MagicMock()
    mock_stream = MagicMock()
    
    pg = ParserGenerator(mock_path, mock_stream)
    
    assert pg.filename == mock_path
    assert pg.stream == mock_stream
    assert isinstance(pg.first, dict)
    assert all(isinstance(k, str) and (v is None or isinstance(v, dict)) for k, v in pg.first.items())
    mock_parse.assert_called_once()
