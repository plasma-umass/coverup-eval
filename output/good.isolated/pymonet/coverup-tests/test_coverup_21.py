# file pymonet/lazy.py:95-104
# lines [95, 102, 103, 104]
# branches ['102->103', '102->104']

import pytest
from pymonet.lazy import Lazy

def test_lazy_get_evaluated():
    lazy_instance = Lazy(lambda: 42)
    # Force evaluation
    value = lazy_instance.get()
    assert lazy_instance.is_evaluated
    # Now get should return the memoized value without recomputing
    assert lazy_instance.get() == value

def test_lazy_get_not_evaluated(mocker):
    compute_value_mock = mocker.Mock(return_value=42)
    lazy_instance = Lazy(compute_value_mock)
    assert not lazy_instance.is_evaluated
    # get should compute the value
    result = lazy_instance.get()
    assert compute_value_mock.called
    assert result == 42
