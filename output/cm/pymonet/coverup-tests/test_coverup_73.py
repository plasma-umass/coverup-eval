# file pymonet/immutable_list.py:24-25
# lines [24, 25]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_str():
    # Create an ImmutableList instance
    immutable_list = ImmutableList([1, 2, 3])

    # Convert to string and assert the correct representation
    str_representation = str(immutable_list)
    assert str_representation == "ImmutableList[[1, 2, 3]]"
