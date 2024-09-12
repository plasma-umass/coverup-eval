# file: f115/__init__.py:1-4
# asked: {"lines": [1, 2, 4], "branches": []}
# gained: {"lines": [1, 2, 4], "branches": []}

import pytest
from f115 import max_fill

def test_max_fill():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    capacity = 5
    result = max_fill(grid, capacity)
    assert result == 10  # (1+2+3)/5 = 1.2 -> 2, (4+5+6)/5 = 3 -> 3, (7+8+9)/5 = 4.8 -> 5, 2+3+5 = 10

def test_max_fill_empty_grid():
    grid = []
    capacity = 5
    result = max_fill(grid, capacity)
    assert result == 0

def test_max_fill_zero_capacity():
    grid = [[1, 2, 3]]
    capacity = 0
    with pytest.raises(ZeroDivisionError):
        max_fill(grid, capacity)
