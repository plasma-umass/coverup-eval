# file py_backwards/utils/helpers.py:12-17
# lines [12, 13, 14, 15, 17]
# branches []

import pytest
from py_backwards.utils.helpers import eager

def test_eager_decorator():
    @eager
    def generate_numbers():
        yield 1
        yield 2
        yield 3

    result = generate_numbers()
    assert isinstance(result, list)
    assert result == [1, 2, 3]
