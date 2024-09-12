# file: f013/__init__.py:1-5
# asked: {"lines": [1, 3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [1, 3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest
from f013 import greatest_common_divisor

def test_greatest_common_divisor():
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(7, 1) == 1
    assert greatest_common_divisor(1, 7) == 1
    assert greatest_common_divisor(0, 0) == 0
