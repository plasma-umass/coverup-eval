# file: f052/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [1, 3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest
from f052 import below_threshold

def test_below_threshold_all_below():
    assert below_threshold([1, 2, 3], 5) == True

def test_below_threshold_one_above(monkeypatch):
    assert below_threshold([1, 2, 6], 5) == False

def test_below_threshold_empty_list():
    assert below_threshold([], 5) == True
