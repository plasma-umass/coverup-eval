# file: py_backwards/utils/helpers.py:12-17
# asked: {"lines": [12, 13, 14, 15, 17], "branches": []}
# gained: {"lines": [12, 13, 14, 15, 17], "branches": []}

import pytest
from py_backwards.utils.helpers import eager

def test_eager_decorator():
    @eager
    def generate_numbers(n):
        for i in range(n):
            yield i

    result = generate_numbers(5)
    assert result == [0, 1, 2, 3, 4]

def test_eager_decorator_empty():
    @eager
    def generate_numbers(n):
        for i in range(n):
            yield i

    result = generate_numbers(0)
    assert result == []

def test_eager_decorator_with_args():
    @eager
    def generate_numbers(n, start=0):
        for i in range(start, n):
            yield i

    result = generate_numbers(5, start=2)
    assert result == [2, 3, 4]
