# file: pymonet/lazy.py:24-25
# asked: {"lines": [24, 25], "branches": []}
# gained: {"lines": [24, 25], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_str(monkeypatch):
    def mock_constructor_fn():
        return 42

    lazy_instance = Lazy(mock_constructor_fn)

    # Mocking the attributes to ensure the __str__ method is called
    monkeypatch.setattr(lazy_instance, 'constructor_fn', 'mock_constructor_fn')
    monkeypatch.setattr(lazy_instance, 'value', 'mock_value')
    monkeypatch.setattr(lazy_instance, 'is_evaluated', 'mock_is_evaluated')

    expected_str = 'Lazy[fn=mock_constructor_fn, value=mock_value, is_evaluated=mock_is_evaluated]'
    assert str(lazy_instance) == expected_str
