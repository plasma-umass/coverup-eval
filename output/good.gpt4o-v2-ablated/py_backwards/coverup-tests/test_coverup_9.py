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

    result = generate_numbers(0)
    assert result == []

    result = generate_numbers(1)
    assert result == [0]

    result = generate_numbers(3)
    assert result == [0, 1, 2]
