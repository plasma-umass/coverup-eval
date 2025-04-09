# file pymonet/immutable_list.py:88-97
# lines [97]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_unshift_creates_new_list_with_element():
    original_list = ImmutableList([2, 3, 4])
    new_element = 1
    new_list = original_list.unshift(new_element)
    
    assert new_list != original_list
    assert new_list.head == new_element
    assert new_list.tail == original_list

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Mock any global state or perform cleanup if necessary
    yield
    # Perform any necessary cleanup here
