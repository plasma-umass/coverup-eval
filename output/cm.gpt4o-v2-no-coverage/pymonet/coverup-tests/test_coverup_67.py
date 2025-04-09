# file: pymonet/lazy.py:139-149
# asked: {"lines": [139, 147, 149], "branches": []}
# gained: {"lines": [139, 147, 149], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.monad_try import Try

def test_lazy_to_try_success(monkeypatch):
    def mock_constructor_fn():
        return 42

    lazy_instance = Lazy(mock_constructor_fn)

    def mock_try_of(fn, *args):
        try:
            result = fn(*args)
            return Try(result, True)
        except Exception as e:
            return Try(e, False)

    monkeypatch.setattr(Try, 'of', mock_try_of)

    result = lazy_instance.to_try()
    assert result.is_success
    assert result.value == 42

def test_lazy_to_try_failure(monkeypatch):
    def mock_constructor_fn():
        raise ValueError("Test error")

    lazy_instance = Lazy(mock_constructor_fn)

    def mock_try_of(fn, *args):
        try:
            result = fn(*args)
            return Try(result, True)
        except Exception as e:
            return Try(e, False)

    monkeypatch.setattr(Try, 'of', mock_try_of)

    result = lazy_instance.to_try()
    assert not result.is_success
    assert isinstance(result.value, ValueError)
    assert str(result.value) == "Test error"
