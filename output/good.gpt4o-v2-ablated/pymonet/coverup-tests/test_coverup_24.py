# file: pymonet/immutable_list.py:99-111
# asked: {"lines": [99, 108, 109, 111], "branches": [[108, 109], [108, 111]]}
# gained: {"lines": [99, 108, 109, 111], "branches": [[108, 109], [108, 111]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_map_with_non_empty_list():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = lst.map(lambda x: x * 2)
    assert result.head == 2
    assert result.tail.head == 4
    assert result.tail.tail.head == 6
    assert result.tail.tail.tail is None

def test_map_with_empty_list():
    lst = ImmutableList(None)
    result = lst.map(lambda x: x if x is not None else 0)
    assert result.head == 0
    assert result.tail is None

def test_map_with_single_element_list():
    lst = ImmutableList(5)
    result = lst.map(lambda x: x + 1)
    assert result.head == 6
    assert result.tail is None

@pytest.fixture
def mock_immutable_list(monkeypatch):
    class MockImmutableList:
        def __init__(self, head, tail=None):
            self.head = head
            self.tail = tail

        def map(self, fn):
            if self.tail is None:
                return MockImmutableList(fn(self.head))
            return MockImmutableList(fn(self.head), self.tail.map(fn))

    monkeypatch.setattr('pymonet.immutable_list.ImmutableList', MockImmutableList)
    return MockImmutableList

def test_map_with_mocked_list(mock_immutable_list):
    lst = mock_immutable_list(1, mock_immutable_list(2, mock_immutable_list(3)))
    result = lst.map(lambda x: x * 2)
    assert result.head == 2
    assert result.tail.head == 4
    assert result.tail.tail.head == 6
    assert result.tail.tail.tail is None
