# file: pymonet/lazy.py:139-149
# asked: {"lines": [139, 147, 149], "branches": []}
# gained: {"lines": [139, 147, 149], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.monad_try import Try

def test_lazy_to_try_success(monkeypatch):
    class MockLazy(Lazy):
        def __init__(self, constructor_fn):
            self.constructor_fn = constructor_fn

    def mock_constructor_fn(*args):
        return "success"

    lazy_instance = MockLazy(mock_constructor_fn)

    result = lazy_instance.to_try()
    assert isinstance(result, Try)
    assert result.is_success
    assert result.value == "success"

def test_lazy_to_try_failure(monkeypatch):
    class MockLazy(Lazy):
        def __init__(self, constructor_fn):
            self.constructor_fn = constructor_fn

    def mock_constructor_fn(*args):
        raise ValueError("failure")

    lazy_instance = MockLazy(mock_constructor_fn)

    result = lazy_instance.to_try()
    assert isinstance(result, Try)
    assert not result.is_success
    assert isinstance(result.value, ValueError)
    assert str(result.value) == "failure"
