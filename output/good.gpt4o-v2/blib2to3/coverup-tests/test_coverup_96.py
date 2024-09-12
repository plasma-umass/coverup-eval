# file: src/blib2to3/pgen2/pgen.py:311-329
# asked: {"lines": [314, 315, 316, 317, 318, 327], "branches": [[313, 314], [326, 327]]}
# gained: {"lines": [314, 315, 316, 317, 318, 327], "branches": [[313, 314], [326, 327]]}

import pytest
from blib2to3.pgen2 import token
from blib2to3.pgen2.pgen import ParserGenerator
from unittest.mock import MagicMock, mock_open, patch

@pytest.fixture
def parser_generator():
    with patch("blib2to3.pgen2.pgen.open", mock_open(read_data="dummy_rule: a\n")) as mock_file:
        pg = ParserGenerator("dummy_filename")
        pg.gettoken = MagicMock()
        pg.parse_rhs = MagicMock()
        pg.expect = MagicMock()
        pg.parse_atom = MagicMock()
        yield pg

def test_parse_item_with_square_brackets(parser_generator):
    parser_generator.value = "["
    a = MagicMock()
    z = MagicMock()
    parser_generator.parse_rhs.return_value = (a, z)
    
    result = parser_generator.parse_item()
    
    parser_generator.gettoken.assert_called_once()
    parser_generator.parse_rhs.assert_called_once()
    parser_generator.expect.assert_called_once_with(token.OP, "]")
    a.addarc.assert_called_once_with(z)
    assert result == (a, z)

def test_parse_item_with_plus_sign(parser_generator):
    parser_generator.value = "+"
    a = MagicMock()
    z = MagicMock()
    parser_generator.parse_atom.return_value = (a, z)
    
    result = parser_generator.parse_item()
    
    parser_generator.gettoken.assert_called_once()
    z.addarc.assert_called_once_with(a)
    assert result == (a, z)

def test_parse_item_with_asterisk(parser_generator):
    parser_generator.value = "*"
    a = MagicMock()
    z = MagicMock()
    parser_generator.parse_atom.return_value = (a, z)
    
    result = parser_generator.parse_item()
    
    parser_generator.gettoken.assert_called_once()
    z.addarc.assert_called_once_with(a)
    assert result == (a, a)
