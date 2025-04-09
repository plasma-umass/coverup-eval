# file: apimd/parser.py:141-153
# asked: {"lines": [141, 151, 152, 153], "branches": []}
# gained: {"lines": [141, 151, 152, 153], "branches": []}

import pytest
from apimd.parser import table

def test_table_with_strings():
    result = table('a', 'b', items=['c', 'd'])
    expected = '| a | b |\n|:---:|:---:|\n| c |\n| d |\n\n'
    assert result == expected

def test_table_with_iterables():
    result = table('a', 'b', items=[['c', 'd'], ['e', 'f']])
    expected = '| a | b |\n|:---:|:---:|\n| c | d |\n| e | f |\n\n'
    assert result == expected

def test_table_with_mixed_items():
    result = table('a', 'b', items=['c', ['d', 'e']])
    expected = '| a | b |\n|:---:|:---:|\n| c |\n| d | e |\n\n'
    assert result == expected
