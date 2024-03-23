# file pymonet/immutable_list.py:152-168
# lines [152, 161, 162, 164, 165, 168]
# branches ['161->162', '161->164', '164->165', '164->168']

import pytest
from pymonet.immutable_list import ImmutableList

class MockImmutableList(ImmutableList):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

@pytest.fixture
def empty_list():
    return MockImmutableList()

@pytest.fixture
def single_element_list():
    return MockImmutableList(head=10)

@pytest.fixture
def multiple_elements_list():
    first = MockImmutableList(head=1)
    second = MockImmutableList(head=2, tail=first)
    return MockImmutableList(head=3, tail=second)

def test_reduce_with_empty_list(empty_list):
    result = empty_list.reduce(lambda acc, x: acc + x, 0)
    assert result == 0

def test_reduce_with_single_element_list(single_element_list):
    result = single_element_list.reduce(lambda acc, x: acc + x, 0)
    assert result == 10

def test_reduce_with_multiple_elements_list(multiple_elements_list):
    result = multiple_elements_list.reduce(lambda acc, x: acc + x, 0)
    assert result == 6
