# file apimd/parser.py:576-578
# lines [576, 578]
# branches []

import pytest
from apimd.parser import Parser

@pytest.fixture
def parser_instance():
    parser = Parser()
    parser.level = {'name1': 1, 'Name2': 2, 'NAME3': 3}
    yield parser

def test_names_cmp(parser_instance):
    # Test with a name that is all lowercase
    result = parser_instance._Parser__names_cmp('name1')
    assert result == (1, 'name1', False)

    # Test with a name that has mixed case
    result = parser_instance._Parser__names_cmp('Name2')
    assert result == (2, 'name2', True)

    # Test with a name that is all uppercase
    result = parser_instance._Parser__names_cmp('NAME3')
    assert result == (3, 'name3', True)
