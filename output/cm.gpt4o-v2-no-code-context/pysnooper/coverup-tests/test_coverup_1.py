# file: pysnooper/utils.py:90-95
# asked: {"lines": [90, 91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [90, 91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

import pytest
from pysnooper.utils import ensure_tuple
from collections.abc import Iterable

def test_ensure_tuple_with_iterable(monkeypatch):
    class MockIterable(Iterable):
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
