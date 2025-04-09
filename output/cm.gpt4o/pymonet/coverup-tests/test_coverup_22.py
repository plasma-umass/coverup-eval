# file pymonet/immutable_list.py:152-168
# lines [152, 161, 162, 164, 165, 168]
# branches ['161->162', '161->164', '164->165', '164->168']

import pytest
from pymonet.immutable_list import ImmutableList

def test_reduce_empty_list():
    lst = ImmutableList()
    result = lst.reduce(lambda acc, x: acc + x, 0)
    assert result == 0

def test_reduce_single_element_list():
    lst = ImmutableList(1)
    result = lst.reduce(lambda acc, x: acc + x, 0)
    assert result == 1

def test_reduce_multiple_elements_list():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = lst.reduce(lambda acc, x: acc + x, 0)
    assert result == 6

def test_reduce_with_non_zero_initial_accumulator():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = lst.reduce(lambda acc, x: acc + x, 10)
    assert result == 16

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # Code to cleanup after tests
