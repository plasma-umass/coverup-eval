# file: f063/__init__.py:1-9
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest
from f063 import fibfib

def test_fibfib_0():
    assert fibfib(0) == 0

def test_fibfib_1():
    assert fibfib(1) == 0

def test_fibfib_2():
    assert fibfib(2) == 1

def test_fibfib_3():
    assert fibfib(3) == 1

def test_fibfib_4():
    assert fibfib(4) == 2

def test_fibfib_5():
    assert fibfib(5) == 4
