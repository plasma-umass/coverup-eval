# file: pymonet/immutable_list.py:24-25
# asked: {"lines": [24, 25], "branches": []}
# gained: {"lines": [24, 25], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_str(monkeypatch):
    class MockImmutableList(ImmutableList):
        def __init__(self, head, tail=None):
            self.head = head
            self.tail = tail

        def to_list(self):
            return [self.head] if self.tail is None else [self.head, *self.tail.to_list()]

    # Create a mock list
    mock_list = MockImmutableList(1, MockImmutableList(2, MockImmutableList(3)))

    # Test the __str__ method
    assert str(mock_list) == 'ImmutableList[1, 2, 3]'
