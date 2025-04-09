# file pymonet/lazy.py:139-149
# lines [139, 147, 149]
# branches []

import pytest
from pymonet.lazy import Lazy
from pymonet.monad_try import Try

def test_lazy_to_try_success():
    def constructor_fn():
        return 42

    lazy_instance = Lazy(constructor_fn)
    result = lazy_instance.to_try()

    assert isinstance(result, Try)
    assert result.is_success
    assert result.get_or_else(None) == 42

def test_lazy_to_try_failure():
    def constructor_fn():
        raise ValueError("Error occurred")

    lazy_instance = Lazy(constructor_fn)
    result = lazy_instance.to_try()

    assert isinstance(result, Try)
    assert not result.is_success
    assert result.get_or_else(None) is None
