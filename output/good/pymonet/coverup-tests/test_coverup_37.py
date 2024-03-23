# file pymonet/monad_try.py:92-105
# lines [92, 103, 104, 105]
# branches ['103->104', '103->105']

import pytest
from pymonet.monad_try import Try

def test_try_filter_success():
    successful_try = Try(42, True)
    filterer = lambda x: x > 40
    filtered_try = successful_try.filter(filterer)
    assert filtered_try.is_success
    assert filtered_try.value == 42

def test_try_filter_failure():
    successful_try = Try(42, True)
    filterer = lambda x: x < 40
    filtered_try = successful_try.filter(filterer)
    assert not filtered_try.is_success
    assert filtered_try.value == 42

def test_try_filter_on_failure():
    failed_try = Try(42, False)
    filterer = lambda x: x > 40
    filtered_try = failed_try.filter(filterer)
    assert not filtered_try.is_success
    assert filtered_try.value == 42
