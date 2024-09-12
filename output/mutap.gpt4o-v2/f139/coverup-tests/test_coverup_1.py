# file: f139/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import pytest
from f139 import special_factorial

def test_special_factorial():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
