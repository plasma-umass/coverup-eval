# file: pymonet/lazy.py:24-25
# asked: {"lines": [24, 25], "branches": []}
# gained: {"lines": [24, 25], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_str(monkeypatch):
    def mock_constructor_fn():
        return 42

    lazy_instance = Lazy(mock_constructor_fn)
    lazy_instance.value = 42
    lazy_instance.is_evaluated = True

    expected_str = 'Lazy[fn={}, value={}, is_evaluated={}]'.format(mock_constructor_fn, 42, True)
    assert str(lazy_instance) == expected_str
