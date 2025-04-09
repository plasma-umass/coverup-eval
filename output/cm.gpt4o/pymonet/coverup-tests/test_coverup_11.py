# file pymonet/immutable_list.py:27-45
# lines [27, 36, 37, 39, 40, 42, 43, 44]
# branches ['36->37', '36->39', '39->40', '39->42']

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_add():
    # Test adding two ImmutableList instances
    list1 = ImmutableList(1, ImmutableList(2, None))
    list2 = ImmutableList(3, ImmutableList(4, None))
    result = list1 + list2

    assert result.head == 1
    assert result.tail.head == 2
    assert result.tail.tail.head == 3
    assert result.tail.tail.tail.head == 4
    assert result.tail.tail.tail.tail is None

    # Test adding an ImmutableList to an empty ImmutableList
    empty_list = ImmutableList(None, None)
    result = empty_list + list2

    assert result.head is None
    assert result.tail.head == 3
    assert result.tail.tail.head == 4
    assert result.tail.tail.tail is None

    # Test adding an ImmutableList to a non-ImmutableList (should raise ValueError)
    with pytest.raises(ValueError, match='ImmutableList: you can not add any other instace than ImmutableList'):
        list1 + [3, 4]

