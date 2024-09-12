# file: apimd/parser.py:141-153
# asked: {"lines": [141, 151, 152, 153], "branches": []}
# gained: {"lines": [141, 151, 152, 153], "branches": []}

import pytest
from apimd.parser import table

def test_table_with_strings():
    titles = ('a', 'b')
    items = [['c', 'd']]
    expected_output = '| a | b |\n|:---:|:---:|\n| c | d |\n\n'
    assert table(*titles, items=items) == expected_output

def test_table_with_iterables():
    titles = ('a', 'b')
    items = [['c', 'd'], ['e', 'f']]
    expected_output = '| a | b |\n|:---:|:---:|\n| c | d |\n| e | f |\n\n'
    assert table(*titles, items=items) == expected_output

def test_table_mixed_items():
    titles = ('a', 'b')
    items = ['c', ['d', 'e']]
    expected_output = '| a | b |\n|:---:|:---:|\n| c |\n| d | e |\n\n'
    assert table(*titles, items=items) == expected_output
