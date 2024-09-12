# file: pymonet/immutable_list.py:66-68
# asked: {"lines": [66, 67, 68], "branches": []}
# gained: {"lines": [66, 67, 68], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_empty():
    empty_list = ImmutableList.empty()
    assert isinstance(empty_list, ImmutableList)
    assert empty_list.is_empty == True
