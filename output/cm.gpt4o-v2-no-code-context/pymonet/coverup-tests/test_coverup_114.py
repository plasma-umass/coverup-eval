# file: pymonet/utils.py:140-165
# asked: {"lines": [154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}
# gained: {"lines": [154, 156, 157, 158, 159, 160, 161, 163, 165], "branches": [[158, 159], [158, 160]]}

import pytest
from pymonet.utils import memoize

def test_memoize_function_called_once():
    call_count = 0

    def sample_function(x):
        nonlocal call_count
        call_count += 1
        return x * 2

    memoized_function = memoize(sample_function)

    assert memoized_function(2) == 4
    assert memoized_function(2) == 4
    assert call_count == 1

def test_memoize_function_called_with_different_args():
    call_count = 0

    def sample_function(x):
        nonlocal call_count
        call_count += 1
        return x * 2

    memoized_function = memoize(sample_function)

    assert memoized_function(2) == 4
    assert memoized_function(3) == 6
    assert call_count == 2

def test_memoize_custom_key():
    call_count = 0

    def sample_function(x):
        nonlocal call_count
        call_count += 1
        return x * 2

    def custom_key(a, b):
        return a % 2 == b % 2

    memoized_function = memoize(sample_function, key=custom_key)

    assert memoized_function(2) == 4
    assert memoized_function(3) == 6
    assert call_count == 2  # 3 is considered different from 2 because of custom_key

def test_memoize_no_cache_hit():
    call_count = 0

    def sample_function(x):
        nonlocal call_count
        call_count += 1
        return x * 2

    memoized_function = memoize(sample_function)

    assert memoized_function(2) == 4
    assert memoized_function(3) == 6
    assert memoized_function(4) == 8
    assert call_count == 3

def test_memoize_cache_hit():
    call_count = 0

    def sample_function(x):
        nonlocal call_count
        call_count += 1
        return x * 2

    memoized_function = memoize(sample_function)

    assert memoized_function(2) == 4
    assert memoized_function(2) == 4
    assert call_count == 1
