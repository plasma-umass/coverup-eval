# file: f129/__init__.py:1-29
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

import pytest
from f129 import minPath

def test_minPath_all_zeros():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    k = 5
    expected = [1, 10, 1, 10, 1]
    assert minPath(grid, k) == expected

def test_minPath_single_one():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    k = 4
    expected = [1, 0, 1, 0]
    assert minPath(grid, k) == expected

def test_minPath_multiple_ones():
    grid = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    k = 3
    expected = [1, 0, 1]
    assert minPath(grid, k) == expected

def test_minPath_edge_case():
    grid = [
        [1, 1],
        [1, 1]
    ]
    k = 2
    expected = [1, 1]
    assert minPath(grid, k) == expected

def test_minPath_large_k():
    grid = [
        [0, 1],
        [1, 0]
    ]
    k = 6
    expected = [1, 0, 1, 0, 1, 0]
    assert minPath(grid, k) == expected
