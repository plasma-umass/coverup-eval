# file: src/blib2to3/pgen2/pgen.py:350-357
# asked: {"lines": [350, 351, 352, 353, 355, 356, 357], "branches": [[351, 352], [351, 355]]}
# gained: {"lines": [350, 351, 352, 353, 355, 356, 357], "branches": [[351, 352], [351, 355]]}

import pytest
from unittest.mock import MagicMock
from blib2to3.pgen2.pgen import ParserGenerator

@pytest.fixture
def parser_generator():
    pg = ParserGenerator.__new__(ParserGenerator)
    pg.type = None
    pg.value = None
    pg.gettoken = MagicMock()
    pg.raise_error = MagicMock(side_effect=SyntaxError)
    return pg

def test_expect_type_mismatch(parser_generator):
    parser_generator.type = 1
    parser_generator.value = 'value'
    with pytest.raises(SyntaxError):
        parser_generator.expect(2, 'value')
    parser_generator.raise_error.assert_called_once_with(
        'expected %s/%s, got %s/%s', 2, 'value', 1, 'value'
    )

def test_expect_value_mismatch(parser_generator):
    parser_generator.type = 1
    parser_generator.value = 'value'
    with pytest.raises(SyntaxError):
        parser_generator.expect(1, 'different_value')
    parser_generator.raise_error.assert_called_once_with(
        'expected %s/%s, got %s/%s', 1, 'different_value', 1, 'value'
    )

def test_expect_success(parser_generator):
    parser_generator.type = 1
    parser_generator.value = 'value'
    result = parser_generator.expect(1, 'value')
    assert result == 'value'
    parser_generator.gettoken.assert_called_once()

def test_expect_success_no_value_check(parser_generator):
    parser_generator.type = 1
    parser_generator.value = 'value'
    result = parser_generator.expect(1)
    assert result == 'value'
    parser_generator.gettoken.assert_called_once()
