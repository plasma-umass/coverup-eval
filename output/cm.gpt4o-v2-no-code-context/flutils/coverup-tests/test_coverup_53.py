# file: flutils/objutils.py:146-203
# asked: {"lines": [146, 201, 202, 203], "branches": [[201, 202], [201, 203]]}
# gained: {"lines": [146, 201, 202, 203], "branches": [[201, 202], [201, 203]]}

import pytest
from collections import UserList, deque
from collections.abc import KeysView, ValuesView, Iterator
from decimal import Decimal
from flutils.objutils import is_list_like

def test_is_list_like_with_list():
    assert is_list_like([1, 2, 3]) is True

def test_is_list_like_with_reversed_list():
    assert is_list_like(reversed([1, 2, 3])) is True

def test_is_list_like_with_string():
    assert is_list_like('hello') is False

def test_is_list_like_with_sorted_string():
    assert is_list_like(sorted('hello')) is True

def test_is_list_like_with_userlist():
    assert is_list_like(UserList([1, 2, 3])) is True

def test_is_list_like_with_deque():
    assert is_list_like(deque([1, 2, 3])) is True

def test_is_list_like_with_keysview():
    assert is_list_like(KeysView({'a': 1, 'b': 2})) is True

def test_is_list_like_with_valuesview():
    assert is_list_like(ValuesView({'a': 1, 'b': 2})) is True

def test_is_list_like_with_frozenset():
    assert is_list_like(frozenset([1, 2, 3])) is True

def test_is_list_like_with_set():
    assert is_list_like(set([1, 2, 3])) is True

def test_is_list_like_with_tuple():
    assert is_list_like((1, 2, 3)) is True

def test_is_list_like_with_none():
    assert is_list_like(None) is False

def test_is_list_like_with_bool():
    assert is_list_like(True) is False

def test_is_list_like_with_bytes():
    assert is_list_like(b'hello') is False

def test_is_list_like_with_decimal():
    assert is_list_like(Decimal('10.5')) is False

def test_is_list_like_with_dict():
    assert is_list_like({'a': 1, 'b': 2}) is False

def test_is_list_like_with_float():
    assert is_list_like(10.5) is False

def test_is_list_like_with_int():
    assert is_list_like(10) is False

def test_is_list_like_with_str():
    assert is_list_like('hello') is False
