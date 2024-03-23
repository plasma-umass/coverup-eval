# file py_backwards/utils/helpers.py:12-17
# lines [12, 13, 14, 15, 17]
# branches []

import pytest
from py_backwards.utils.helpers import eager

def test_eager_decorator():
    # Define a generator function to be decorated
    def some_generator_function(n):
        for i in range(n):
            yield i

    # Decorate the generator function with eager
    eager_function = eager(some_generator_function)

    # Call the decorated function
    result = eager_function(5)

    # Check if the result is a list
    assert isinstance(result, list), "The result should be a list"

    # Check if the result contains all elements from the generator
    assert result == [0, 1, 2, 3, 4], "The result should contain all elements generated"

    # Check if the eager decorator does not affect the original function
    original_result = list(some_generator_function(5))
    assert original_result == [0, 1, 2, 3, 4], "The original function should not be affected by the decorator"
