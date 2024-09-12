# file: f084/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f084 import solve

def test_solve():
    assert solve(123) == '110'
    assert solve(0) == '0'
    assert solve(999) == '11011'
    assert solve(1) == '1'
    assert solve(10) == '1'
    assert solve(111) == '11'
