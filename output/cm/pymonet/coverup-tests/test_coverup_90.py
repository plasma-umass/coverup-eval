# file pymonet/immutable_list.py:113-130
# lines [113, 122, 123, 124, 125, 127, 128, 130]
# branches ['122->123', '122->127', '123->124', '123->125', '127->128', '127->130']

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_filter(mocker):
    # Mock the callable to control the filter behavior
    mock_fn = mocker.Mock(side_effect=lambda x: x is not None and x > 10)

    # Create an ImmutableList with elements
    list_with_elements = ImmutableList(5, ImmutableList(15, ImmutableList(20)))

    # Filter the list
    filtered_list = list_with_elements.filter(mock_fn)

    # Convert filtered ImmutableList to a regular list for easy assertion
    result = []
    while filtered_list and not filtered_list.is_empty:
        result.append(filtered_list.head)
        filtered_list = filtered_list.tail

    # Assertions to check if the filter worked correctly
    assert result == [15, 20]  # Only elements greater than 10 should remain

    # Test with an ImmutableList with a single element
    single_element_list = ImmutableList(5)
    filtered_single_element_list = single_element_list.filter(mock_fn)

    # Convert filtered ImmutableList to a regular list for easy assertion
    single_result = []
    while filtered_single_element_list and not filtered_single_element_list.is_empty:
        single_result.append(filtered_single_element_list.head)
        filtered_single_element_list = filtered_single_element_list.tail

    # Assertions to check if the filter worked correctly
    assert single_result == []  # The single element does not satisfy the condition

    # Test with an ImmutableList with no elements
    empty_list = ImmutableList(is_empty=True)
    filtered_empty_list = empty_list.filter(mock_fn)

    # Convert filtered ImmutableList to a regular list for easy assertion
    empty_result = []
    while filtered_empty_list and not filtered_empty_list.is_empty:
        empty_result.append(filtered_empty_list.head)
        filtered_empty_list = filtered_empty_list.tail

    # Assertions to check if the filter worked correctly
    assert empty_result == []  # There should be no elements as the list was empty

    # Clean up the mock
    mocker.stopall()
