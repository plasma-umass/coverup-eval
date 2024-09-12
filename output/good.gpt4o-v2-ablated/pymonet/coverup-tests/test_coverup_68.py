# file: pymonet/utils.py:140-165
# asked: {"lines": [154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}
# gained: {"lines": [154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}

import pytest
from typing import Callable, Any, List

# Assuming the memoize function is defined in pymonet/utils.py
from pymonet.utils import memoize

def test_memoize_function_caching():
    def sample_function(x):
        return x * 2

    memoized_sample_function = memoize(sample_function)

    # Test that the function returns the correct result
    assert memoized_sample_function(2) == 4
    assert memoized_sample_function(3) == 6

    # Test that the function caches results
    assert memoized_sample_function(2) == 4  # This should hit the cache
    assert memoized_sample_function(3) == 6  # This should hit the cache

def test_memoize_custom_key():
    def sample_function(x):
        return x * 2

    def custom_key(a, b):
        return a == b

    memoized_sample_function = memoize(sample_function, key=custom_key)

    # Test that the function returns the correct result
    assert memoized_sample_function(2) == 4
    assert memoized_sample_function(3) == 6

    # Test that the function caches results with custom key
    assert memoized_sample_function(2) == 4  # This should hit the cache
    assert memoized_sample_function(3) == 6  # This should hit the cache

def test_memoize_no_cache_hit():
    def sample_function(x):
        return x * 2

    memoized_sample_function = memoize(sample_function)

    # Test that the function returns the correct result
    assert memoized_sample_function(2) == 4
    assert memoized_sample_function(3) == 6

    # Test that the function does not hit the cache for new arguments
    assert memoized_sample_function(4) == 8  # This should not hit the cache

@pytest.fixture
def mock_find(mocker):
    return mocker.patch('pymonet.utils.find')

def test_memoize_with_mocked_find(mock_find):
    def sample_function(x):
        return x * 2

    mock_find.return_value = None
    memoized_sample_function = memoize(sample_function)

    # Test that the function returns the correct result
    assert memoized_sample_function(2) == 4
    assert memoized_sample_function(3) == 6

    # Ensure find was called
    assert mock_find.call_count == 2

    # Test that the function caches results
    mock_find.return_value = (2, 4)
    assert memoized_sample_function(2) == 4  # This should hit the cache

    # Ensure find was called again
    assert mock_find.call_count == 3
