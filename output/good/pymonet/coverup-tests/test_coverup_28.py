# file pymonet/immutable_list.py:66-68
# lines [66, 67, 68]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_empty():
    # Test the ImmutableList.empty() class method
    empty_list = ImmutableList.empty()
    assert isinstance(empty_list, ImmutableList)
    assert empty_list.is_empty == True
