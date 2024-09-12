# file: apimd/parser.py:576-578
# asked: {"lines": [576, 578], "branches": []}
# gained: {"lines": [576, 578], "branches": []}

import pytest
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser()

def test_names_cmp(parser):
    # Setup
    parser.level = {'Test': 1, 'test': 2, 'TEST': 3}

    # Test with mixed case
    result = parser._Parser__names_cmp('Test')
    assert result == (1, 'test', True)

    # Test with lower case
    result = parser._Parser__names_cmp('test')
    assert result == (2, 'test', False)

    # Test with upper case
    result = parser._Parser__names_cmp('TEST')
    assert result == (3, 'test', True)
