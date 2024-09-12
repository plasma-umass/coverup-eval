# file: typesystem/unique.py:20-22
# asked: {"lines": [20, 21, 22], "branches": []}
# gained: {"lines": [20, 21, 22], "branches": []}

import pytest
from typesystem.unique import Uniqueness

def test_uniqueness_contains_with_true():
    unique = Uniqueness()
    unique._set.add(unique.TRUE)
    assert True in unique

def test_uniqueness_contains_with_false():
    unique = Uniqueness()
    unique._set.add(unique.FALSE)
    assert False in unique

def test_uniqueness_contains_with_list():
    unique = Uniqueness()
    test_list = [1, 2, 3]
    unique._set.add(('list', (1, 2, 3)))
    assert test_list in unique

def test_uniqueness_contains_with_dict():
    unique = Uniqueness()
    test_dict = {'a': 1, 'b': 2}
    unique._set.add(('dict', (('a', 1), ('b', 2))))
    assert test_dict in unique
