# file: pymonet/box.py:59-68
# asked: {"lines": [59, 66, 68], "branches": []}
# gained: {"lines": [59, 66, 68], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

def test_box_to_maybe(monkeypatch):
    class MockMaybe:
        def __init__(self, value):
            self.value = value

        @classmethod
        def just(cls, value):
            return cls(value)

        def get(self):
            return self.value

    monkeypatch.setattr("pymonet.maybe.Maybe", MockMaybe)

    box = Box(42)
    maybe = box.to_maybe()
    assert isinstance(maybe, MockMaybe)
    assert maybe.get() == 42
