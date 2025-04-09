# file pymonet/immutable_list.py:71-75
# lines [71, 72, 73, 75]
# branches ['72->73', '72->75']

import pytest
from pymonet.immutable_list import ImmutableList

@pytest.fixture
def single_element_list():
    return ImmutableList(1, None)

@pytest.fixture
def multi_element_list(single_element_list):
    return ImmutableList(2, single_element_list)

def test_to_list_with_single_element(single_element_list):
    result = single_element_list.to_list()
    assert result == [1], "to_list should return a list with a single element"

def test_to_list_with_multiple_elements(multi_element_list):
    result = multi_element_list.to_list()
    assert result == [2, 1], "to_list should return a list with multiple elements"
