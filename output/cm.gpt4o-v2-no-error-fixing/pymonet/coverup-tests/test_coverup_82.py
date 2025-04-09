# file: pymonet/immutable_list.py:24-25
# asked: {"lines": [24, 25], "branches": []}
# gained: {"lines": [24, 25], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_str():
    # Create an ImmutableList instance
    lst = ImmutableList.of(1, 2, 3)
    
    # Check the string representation
    assert str(lst) == 'ImmutableList[1, 2, 3]'

    # Clean up
    del lst
