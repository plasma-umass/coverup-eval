# file: apimd/parser.py:576-578
# asked: {"lines": [576, 578], "branches": []}
# gained: {"lines": [576, 578], "branches": []}

import pytest
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser()

def test_names_cmp(parser, monkeypatch):
    # Mock the 'level' attribute of the parser instance
    monkeypatch.setattr(parser, 'level', {'Test': 1, 'example': 2})

    # Test with a string that is not all lowercase
    result = parser._Parser__names_cmp('Test')
    assert result == (1, 'test', True)

    # Test with a string that is all lowercase
    result = parser._Parser__names_cmp('example')
    assert result == (2, 'example', False)
