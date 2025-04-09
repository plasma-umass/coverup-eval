# file: pymonet/utils.py:9-22
# asked: {"lines": [9, 15, 16, 18, 19, 20, 21, 22], "branches": [[15, 16], [15, 18], [19, 20], [19, 21]]}
# gained: {"lines": [9, 15, 16, 18, 19, 20, 21, 22], "branches": [[15, 16], [15, 18], [19, 20], [19, 21]]}

import pytest
from pymonet.utils import curry

def test_curry_no_args_count():
    @curry
    def add(a, b):
        return a + b

    assert add(1)(2) == 3

def test_curry_with_args_count():
    def add(a, b):
        return a + b

    curried_add = curry(add, 2)
    assert curried_add(1)(2) == 3

def test_curry_partial_application():
    def add(a, b, c):
        return a + b + c

    curried_add = curry(add)
    add_ab = curried_add(1, 2)
    assert add_ab(3) == 6

def test_curry_full_application():
    def add(a, b, c):
        return a + b + c

    curried_add = curry(add)
    assert curried_add(1)(2)(3) == 6
