# file: pymonet/immutable_list.py:71-75
# asked: {"lines": [71, 72, 73, 75], "branches": [[72, 73], [72, 75]]}
# gained: {"lines": [71, 72, 73, 75], "branches": [[72, 73], [72, 75]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_to_list_single_element():
    # Create an ImmutableList with a single element
    single_element_list = ImmutableList(1)
    # Convert to list and assert the result
    assert single_element_list.to_list() == [1]

def test_to_list_multiple_elements():
    # Create an ImmutableList with multiple elements
    tail_list = ImmutableList(2, ImmutableList(3))
    multi_element_list = ImmutableList(1, tail_list)
    # Convert to list and assert the result
    assert multi_element_list.to_list() == [1, 2, 3]

def test_to_list_empty_tail():
    # Create an ImmutableList with a head and an empty tail
    empty_tail_list = ImmutableList(1, None)
    # Convert to list and assert the result
    assert empty_tail_list.to_list() == [1]

@pytest.fixture
def cleanup():
    # Cleanup fixture to avoid state pollution
    yield
    # Perform any necessary cleanup here

def test_to_list_with_cleanup(cleanup):
    # Create an ImmutableList with multiple elements
    tail_list = ImmutableList(2, ImmutableList(3))
    multi_element_list = ImmutableList(1, tail_list)
    # Convert to list and assert the result
    assert multi_element_list.to_list() == [1, 2, 3]
