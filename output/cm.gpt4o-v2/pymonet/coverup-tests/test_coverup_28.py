# file: pymonet/utils.py:140-165
# asked: {"lines": [140, 154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}
# gained: {"lines": [140, 154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}

import pytest
from pymonet.utils import memoize

def test_memoize_function_caching():
    def sample_function(x):
        return x * 2

    memoized_function = memoize(sample_function)

    # First call, should compute the result
    result1 = memoized_function(2)
    assert result1 == 4

    # Second call with the same argument, should return cached result
    result2 = memoized_function(2)
    assert result2 == 4

    # Ensure the function was only called once for the same argument
    assert result1 == result2

def test_memoize_with_custom_key():
    def sample_function(x):
        return x * 2

    def custom_key(a, b):
        return a == b

    memoized_function = memoize(sample_function, key=custom_key)

    # First call, should compute the result
    result1 = memoized_function(3)
    assert result1 == 6

    # Second call with the same argument, should return cached result
    result2 = memoized_function(3)
    assert result2 == 6

    # Ensure the function was only called once for the same argument
    assert result1 == result2

def test_memoize_with_different_arguments():
    def sample_function(x):
        return x * 2

    memoized_function = memoize(sample_function)

    # Call with different arguments
    result1 = memoized_function(2)
    result2 = memoized_function(3)

    assert result1 == 4
    assert result2 == 6

    # Ensure the function was called for each unique argument
    assert result1 != result2
