# file: pymonet/utils.py:9-22
# asked: {"lines": [9, 15, 16, 18, 19, 20, 21, 22], "branches": [[15, 16], [15, 18], [19, 20], [19, 21]]}
# gained: {"lines": [9, 15, 16, 18, 19, 20, 21, 22], "branches": [[15, 16], [15, 18], [19, 20], [19, 21]]}

import pytest
from pymonet.utils import curry

def test_curry_with_args_count():
    def add(x, y):
        return x + y

    curried_add = curry(add, 2)
    assert curried_add(1)(2) == 3

def test_curry_without_args_count():
    def add(x, y):
        return x + y

    curried_add = curry(add)
    assert curried_add(1)(2) == 3

def test_curry_partial_application():
    def add(x, y, z):
        return x + y + z

    curried_add = curry(add)
    add_two = curried_add(1)(1)
    assert add_two(1) == 3
    assert add_two(2) == 4

def test_curry_no_args():
    def constant():
        return 42

    curried_constant = curry(constant)
    assert curried_constant() == 42
