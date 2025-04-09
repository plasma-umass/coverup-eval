# file: apimd/parser.py:576-578
# asked: {"lines": [576, 578], "branches": []}
# gained: {"lines": [576, 578], "branches": []}

import pytest
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser()

def test_names_cmp(parser):
    parser.level = {'Test': 1, 'example': 2}
    
    result = parser._Parser__names_cmp('Test')
    assert result == (1, 'test', True)
    
    result = parser._Parser__names_cmp('example')
    assert result == (2, 'example', False)
