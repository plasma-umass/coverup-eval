# file: pymonet/utils.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.utils import increase

def test_increase():
    # Test with a positive integer
    assert increase(1) == 2

    # Test with zero
    assert increase(0) == 1

    # Test with a negative integer
    assert increase(-1) == 0

    # Test with a large integer
    assert increase(1000000) == 1000001

    # Test with the minimum integer value
    assert increase(-2147483648) == -2147483647

    # Test with the maximum integer value
    assert increase(2147483647) == 2147483648
