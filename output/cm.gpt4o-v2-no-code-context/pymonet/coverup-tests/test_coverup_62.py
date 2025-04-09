# file: pymonet/immutable_list.py:24-25
# asked: {"lines": [24, 25], "branches": []}
# gained: {"lines": [24, 25], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_str(monkeypatch):
    class MockImmutableList(ImmutableList):
        def to_list(self):
            return [1, 2, 3]

    mock_list = MockImmutableList()
    result = str(mock_list)
    assert result == 'ImmutableList[1, 2, 3]'
