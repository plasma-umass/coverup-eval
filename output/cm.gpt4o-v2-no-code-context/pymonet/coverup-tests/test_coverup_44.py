# file: pymonet/box.py:92-101
# asked: {"lines": [92, 99, 101], "branches": []}
# gained: {"lines": [92, 99, 101], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.monad_try import Try

def test_box_to_try_success(monkeypatch):
    class MockTry:
        def __init__(self, value, is_success):
            self.value = value
            self.is_success = is_success

    monkeypatch.setattr('pymonet.monad_try.Try', MockTry)

    box = Box(42)
    result = box.to_try()

    assert isinstance(result, MockTry)
    assert result.value == 42
    assert result.is_success is True
