# file: pysnooper/utils.py:90-95
# asked: {"lines": [90, 91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [90, 91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

import pytest
from pysnooper.utils import ensure_tuple
from collections.abc import Iterable
import collections.abc as collections_abc
import six

def test_ensure_tuple_with_iterable(monkeypatch):
    class MockIterable:
        def __iter__(self):
            yield 1
            yield 2

    mock_iterable = MockIterable()
    result = ensure_tuple(mock_iterable)
    assert result == (1, 2)

def test_ensure_tuple_with_string():
    result = ensure_tuple("test")
    assert result == ("test",)

def test_ensure_tuple_with_non_iterable():
    result = ensure_tuple(42)
    assert result == (42,)

def test_ensure_tuple_with_list():
    result = ensure_tuple([1, 2, 3])
    assert result == (1, 2, 3)

def test_ensure_tuple_with_tuple():
    result = ensure_tuple((1, 2, 3))
    assert result == (1, 2, 3)

def test_ensure_tuple_with_dict():
    result = ensure_tuple({'a': 1, 'b': 2})
    assert result == ('a', 'b')

def test_ensure_tuple_with_set():
    result = ensure_tuple({1, 2, 3})
    assert result == (1, 2, 3) or result == (2, 1, 3) or result == (3, 2, 1) or result == (1, 3, 2) or result == (2, 3, 1) or result == (3, 1, 2)
