# file pymonet/immutable_list.py:24-25
# lines [24, 25]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_str():
    # Create an instance of ImmutableList
    immutable_list = ImmutableList([1, 2, 3])
    
    # Verify the string representation
    assert str(immutable_list) == 'ImmutableList[[1, 2, 3]]'
