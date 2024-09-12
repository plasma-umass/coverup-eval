# file: f087/__init__.py:1-4
# asked: {"lines": [1, 3, 4], "branches": []}
# gained: {"lines": [1, 3, 4], "branches": []}

import pytest
from f087 import get_row

def test_get_row():
    lst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    x = 5
    expected_output = [(1, 1)]
    assert get_row(lst, x) == expected_output

    x = 10
    expected_output = []
    assert get_row(lst, x) == expected_output

    lst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 5, 9]
    ]
    x = 5
    expected_output = [(1, 1), (2, 1)]
    assert get_row(lst, x) == expected_output

    lst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 5]
    ]
    x = 5
    expected_output = [(1, 1), (2, 2)]
    assert get_row(lst, x) == expected_output

    lst = [
        [1, 2, 3],
        [4, 5, 6],
        [5, 8, 9]
    ]
    x = 5
    expected_output = [(1, 1), (2, 0)]
    assert get_row(lst, x) == expected_output
