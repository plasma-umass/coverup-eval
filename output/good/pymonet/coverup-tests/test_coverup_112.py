# file pymonet/immutable_list.py:132-150
# lines [142, 148]
# branches ['141->142', '147->148']

import pytest
from pymonet.immutable_list import ImmutableList

def test_find_method_executes_missing_lines(mocker):
    # Mock the ImmutableList with a single element to test line 142
    empty_list = ImmutableList()
    assert empty_list.find(lambda x: True) is None

    # Mock the ImmutableList with two elements to test line 148
    list_with_two_elements = ImmutableList(1, ImmutableList(2, None))
    assert list_with_two_elements.find(lambda x: x == 1) == 1

    # Ensure that the test does not affect other tests by not modifying any global state
