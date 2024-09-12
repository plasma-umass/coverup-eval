# file: typesystem/unique.py:28-59
# asked: {"lines": [28, 34, 35, 38, 40, 41, 43, 44, 46, 47, 49, 50, 51, 52, 53, 54, 59], "branches": [[38, 40], [38, 41], [41, 43], [41, 44], [44, 46], [44, 47], [47, 49], [47, 59]]}
# gained: {"lines": [28, 34, 35, 38, 40, 41, 43, 44, 46, 47, 49, 50, 51, 52, 53, 54, 59], "branches": [[38, 40], [38, 41], [41, 43], [41, 44], [44, 46], [44, 47], [47, 49], [47, 59]]}

import pytest
from typesystem.unique import Uniqueness

def test_make_hashable_none():
    u = Uniqueness()
    assert u.make_hashable(None) is None

def test_make_hashable_true():
    u = Uniqueness()
    assert u.make_hashable(True) is u.TRUE

def test_make_hashable_false():
    u = Uniqueness()
    assert u.make_hashable(False) is u.FALSE

def test_make_hashable_list(monkeypatch):
    u = Uniqueness()
    test_list = [1, 2, 3]
    expected = ('list', (1, 2, 3))
    assert u.make_hashable(test_list) == expected

def test_make_hashable_dict(monkeypatch):
    u = Uniqueness()
    test_dict = {'a': 1, 'b': 2}
    expected = ('dict', (('a', 1), ('b', 2)))
    assert u.make_hashable(test_dict) == expected

def test_make_hashable_primitive():
    u = Uniqueness()
    assert u.make_hashable(1) == 1
    assert u.make_hashable(3.14) == 3.14
    assert u.make_hashable("string") == "string"
