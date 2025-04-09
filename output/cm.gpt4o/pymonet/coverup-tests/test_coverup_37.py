# file pymonet/immutable_list.py:66-68
# lines [66, 67, 68]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_empty():
    # Create an empty ImmutableList
    empty_list = ImmutableList.empty()
    
    # Assert that the list is indeed empty
    assert empty_list.is_empty == True
