# file pymonet/utils.py:140-165
# lines [140, 154, 156, 157, 158, 159, 160, 161, 163, 165]
# branches ['158->159', '158->160']

import pytest
from pymonet.utils import memoize

def test_memoize():
    # Setup
    def test_fn(x):
        return x * 2

    def custom_key(a, b):
        return a % 10 == b % 10

    memoized_test_fn = memoize(test_fn, key=custom_key)

    # Test that the function caches correctly with custom key
    assert memoized_test_fn(10) == 20
    assert memoized_test_fn(20) == 20  # Should return cached result because 10 % 10 == 20 % 10

    # Test that the function does not cache with different key
    assert memoized_test_fn(11) == 22  # Different key, should compute again

    # Cleanup is not necessary as the cache is function-local and will not persist between tests
