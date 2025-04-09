# file: src/blib2to3/pgen2/pgen.py:40-53
# asked: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": [[42, 43], [42, 45], [50, 51], [50, 52]]}
# gained: {"lines": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], "branches": [[42, 43], [42, 45], [50, 51], [50, 52]]}

import pytest
from unittest.mock import mock_open, patch
from blib2to3.pgen2.pgen import ParserGenerator
from blib2to3.pgen2 import tokenize
from pathlib import Path

@pytest.fixture
def mock_tokenize_generate_tokens(mocker):
    return mocker.patch('blib2to3.pgen2.tokenize.generate_tokens', return_value=iter([
        (tokenize.NAME, 'name', (1, 0), (1, 4), 'name'),
        (tokenize.OP, ':', (1, 5), (1, 6), ':'),
        (tokenize.STRING, 'value', (1, 7), (1, 12), 'value'),
        (tokenize.NEWLINE, '\n', (1, 13), (1, 14), '\n'),
        (tokenize.ENDMARKER, '', (2, 0), (2, 0), '')
    ]))

def test_parser_generator_init_with_stream(mock_tokenize_generate_tokens):
    mock_stream = mock_open(read_data='name: "value"\n')
    with patch('builtins.open', mock_stream):
        stream = open('dummy')
        pg = ParserGenerator(Path('dummy'), stream)
        assert pg.filename == Path('dummy')
        assert pg.stream == stream
        assert isinstance(pg.generator, type(tokenize.generate_tokens(stream.readline)))
        assert pg.dfas is not None
        assert pg.startsymbol is not None
        assert 'name' in pg.first
        assert 'value' in pg.first['name']

def test_parser_generator_init_without_stream(mock_tokenize_generate_tokens):
    mock_stream = mock_open(read_data='name: "value"\n')
    with patch('builtins.open', mock_stream):
        pg = ParserGenerator(Path('dummy'))
        assert pg.filename == Path('dummy')
        assert pg.stream is not None
        assert isinstance(pg.generator, type(tokenize.generate_tokens(pg.stream.readline)))
        assert pg.dfas is not None
        assert pg.startsymbol is not None
        assert 'name' in pg.first
        assert 'value' in pg.first['name']
