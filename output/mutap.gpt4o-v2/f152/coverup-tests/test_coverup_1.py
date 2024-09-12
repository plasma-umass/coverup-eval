# file: f152/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f152 import compare

def test_compare():
    game = [1, 2, 3]
    guess = [3, 2, 1]
    expected = [2, 0, 2]
    result = compare(game, guess)
    assert result == expected

def test_compare_empty():
    game = []
    guess = []
    expected = []
    result = compare(game, guess)
    assert result == expected

def test_compare_different_lengths():
    game = [1, 2, 3]
    guess = [1, 2]
    expected = [0, 0]
    result = compare(game, guess)
    assert result == expected
