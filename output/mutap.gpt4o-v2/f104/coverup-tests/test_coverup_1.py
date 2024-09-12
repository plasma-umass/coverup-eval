# file: f104/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f104 import unique_digits

def test_unique_digits_all_odd():
    result = unique_digits([135, 579, 333])
    assert result == [135, 333, 579]

def test_unique_digits_mixed():
    result = unique_digits([135, 246, 579, 123])
    assert result == [135, 579]

def test_unique_digits_no_odd():
    result = unique_digits([246, 802, 460])
    assert result == []

def test_unique_digits_empty():
    result = unique_digits([])
    assert result == []

def test_unique_digits_cleanup(monkeypatch):
    # Ensure no state pollution
    monkeypatch.setattr('f104.unique_digits', unique_digits)
    result = unique_digits([135, 579, 333])
    assert result == [135, 333, 579]
