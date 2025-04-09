# file: apimd/parser.py:576-578
# asked: {"lines": [576, 578], "branches": []}
# gained: {"lines": [576, 578], "branches": []}

import pytest
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser(level={'a': 1, 'B': 2, 'c': 3})

def test_names_cmp_lowercase(parser):
    result = parser._Parser__names_cmp('a')
    assert result == (1, 'a', False)

def test_names_cmp_uppercase(parser):
    result = parser._Parser__names_cmp('B')
    assert result == (2, 'b', True)

def test_names_cmp_mixedcase(parser):
    result = parser._Parser__names_cmp('c')
    assert result == (3, 'c', False)
