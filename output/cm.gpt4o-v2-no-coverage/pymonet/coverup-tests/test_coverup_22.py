# file: pymonet/utils.py:140-165
# asked: {"lines": [140, 154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}
# gained: {"lines": [140, 154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}

import pytest
from pymonet.utils import memoize
from pymonet.utils import eq

def test_memoize():
    def sample_function(x):
        return x * 2

    memoized_function = memoize(sample_function, key=eq)

    # Test that the function returns correct results
    assert memoized_function(2) == 4
    assert memoized_function(3) == 6

    # Test that the function uses cache
    assert memoized_function(2) == 4  # This should hit the cache
    assert memoized_function(3) == 6  # This should hit the cache

    # Test with different arguments
    assert memoized_function(4) == 8
    assert memoized_function(5) == 10

    # Test that the function uses cache for new arguments
    assert memoized_function(4) == 8  # This should hit the cache
    assert memoized_function(5) == 10  # This should hit the cache

