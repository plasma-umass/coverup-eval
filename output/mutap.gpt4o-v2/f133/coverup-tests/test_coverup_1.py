# file: f133/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest
import math
from f133 import sum_squares

def test_sum_squares():
    # Test with an empty list
    assert sum_squares([]) == 0

    # Test with positive integers
    assert sum_squares([1, 2, 3]) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

    # Test with negative integers
    assert sum_squares([-1, -2, -3]) == 14  # ceil(-1)^2 + ceil(-2)^2 + ceil(-3)^2 = 1 + 4 + 9 = 14

    # Test with mixed integers
    assert sum_squares([-1, 2, -3, 4]) == 30  # ceil(-1)^2 + ceil(2)^2 + ceil(-3)^2 + ceil(4)^2 = 1 + 4 + 9 + 16 = 30

    # Test with floating point numbers
    assert sum_squares([1.2, 2.5, 3.7]) == 29  # ceil(1.2)^2 + ceil(2.5)^2 + ceil(3.7)^2 = 4 + 9 + 16 = 29

    # Test with mixed floating point and integer numbers
    assert sum_squares([1.2, -2.5, 3, -4.7]) == 33  # ceil(1.2)^2 + ceil(-2.5)^2 + ceil(3)^2 + ceil(-4.7)^2 = 4 + 9 + 9 + 25 = 33
