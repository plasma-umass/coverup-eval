# file: f159/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [1, 3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest
from f159 import eat

def test_eat_need_less_than_remaining():
    result = eat(5, 3, 10)
    assert result == [8, 7], f"Expected [8, 7] but got {result}"

def test_eat_need_equal_to_remaining():
    result = eat(5, 10, 10)
    assert result == [15, 0], f"Expected [15, 0] but got {result}"

def test_eat_need_greater_than_remaining():
    result = eat(5, 15, 10)
    assert result == [15, 0], f"Expected [15, 0] but got {result}"
