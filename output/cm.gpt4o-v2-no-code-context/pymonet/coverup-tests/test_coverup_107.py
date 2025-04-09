# file: pymonet/box.py:81-90
# asked: {"lines": [88, 90], "branches": []}
# gained: {"lines": [88, 90], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.lazy import Lazy

def test_box_to_lazy(monkeypatch):
    class MockLazy:
        def __init__(self, func):
            self.func = func

    monkeypatch.setattr('pymonet.lazy.Lazy', MockLazy)

    box = Box(42)
    lazy = box.to_lazy()

    assert isinstance(lazy, MockLazy)
    assert lazy.func() == 42
