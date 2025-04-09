# file: pymonet/utils.py:140-165
# asked: {"lines": [154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}
# gained: {"lines": [154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}

import pytest
from pymonet.utils import memoize

def test_memoize():
    # Define a simple function to memoize
    def square(x):
        return x * x

    # Memoize the function
    memoized_square = memoize(square)

    # Test that the memoized function returns the correct result
    assert memoized_square(2) == 4
    assert memoized_square(3) == 9

    # Test that the memoized function caches results
    assert memoized_square(2) == 4  # This should hit the cache
    assert memoized_square(3) == 9  # This should hit the cache

    # Test with a different key function
    def custom_key(a, b):
        return a % 10 == b % 10

    memoized_square_custom_key = memoize(square, key=custom_key)
    assert memoized_square_custom_key(2) == 4
    assert memoized_square_custom_key(12) == 4  # This should hit the cache due to custom key

    # Test that the cache is used correctly
    assert memoized_square_custom_key(22) == 4  # This should hit the cache due to custom key

    # Test with a more complex function
    def complex_fn(x):
        return x ** 3 + x ** 2 + x

    memoized_complex_fn = memoize(complex_fn)
    assert memoized_complex_fn(2) == 14
    assert memoized_complex_fn(3) == 39
    assert memoized_complex_fn(2) == 14  # This should hit the cache

    # Test that the cache is used correctly
    assert memoized_complex_fn(3) == 39  # This should hit the cache

    # Test with a different type of argument
    def string_fn(s):
        return s.upper()

    memoized_string_fn = memoize(string_fn)
    assert memoized_string_fn("hello") == "HELLO"
    assert memoized_string_fn("world") == "WORLD"
    assert memoized_string_fn("hello") == "HELLO"  # This should hit the cache

    # Test that the cache is used correctly
    assert memoized_string_fn("world") == "WORLD"  # This should hit the cache
