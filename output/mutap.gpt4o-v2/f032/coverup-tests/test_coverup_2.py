# file: f032/__init__.py:9-21
# asked: {"lines": [9, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [9, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest
from f032 import find_zero

def test_find_zero():
    # Test case where the polynomial has a root between -1 and 1
    xs = [1, 0, -1]  # x^2 - 1 = 0 has roots at x = -1 and x = 1
    result = find_zero(xs)
    assert abs(result - (-1)) < 1e-10 or abs(result - 1) < 1e-10

    # Test case where the polynomial has a root at 0
    xs = [0, 1, 0]  # x = 0 has a root at x = 0
    result = find_zero(xs)
    assert abs(result) < 1e-10

    # Test case where the polynomial has no real roots
    xs = [1, 0, 1]  # x^2 + 1 = 0 has no real roots
    with pytest.raises(OverflowError):
        find_zero(xs)
