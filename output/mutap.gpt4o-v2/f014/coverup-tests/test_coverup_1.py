# file: f014/__init__.py:4-10
# asked: {"lines": [4, 6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [4, 6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}

import pytest
from f014 import all_prefixes

def test_all_prefixes_empty_string():
    assert all_prefixes('') == []

def test_all_prefixes_single_character():
    assert all_prefixes('a') == ['a']

def test_all_prefixes_multiple_characters():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

def test_all_prefixes_with_spaces():
    assert all_prefixes('a b') == ['a', 'a ', 'a b']

def test_all_prefixes_with_special_characters():
    assert all_prefixes('a!b') == ['a', 'a!', 'a!b']
