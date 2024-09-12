# file: f022/__init__.py:4-6
# asked: {"lines": [4, 6], "branches": []}
# gained: {"lines": [4, 6], "branches": []}

import pytest
from f022 import filter_integers

def test_filter_integers_with_integers():
    result = filter_integers([1, 2, 3, 4])
    assert result == [1, 2, 3, 4]

def test_filter_integers_with_mixed_types():
    result = filter_integers([1, 'a', 2.5, 3, None, 4])
    assert result == [1, 3, 4]

def test_filter_integers_with_no_integers():
    result = filter_integers(['a', 2.5, None])
    assert result == []

def test_filter_integers_with_empty_list():
    result = filter_integers([])
    assert result == []
