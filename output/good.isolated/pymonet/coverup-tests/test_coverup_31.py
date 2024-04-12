# file pymonet/immutable_list.py:27-45
# lines [27, 36, 37, 39, 40, 42, 43, 44]
# branches ['36->37', '36->39', '39->40', '39->42']

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_addition():
    list1 = ImmutableList(1, ImmutableList(2, None))
    list2 = ImmutableList(3, ImmutableList(4, None))

    # Test addition of two ImmutableList instances
    result = list1 + list2
    assert isinstance(result, ImmutableList), "Result of addition should be an ImmutableList"
    assert result.head == 1, "Head of the result should be the head of the first list"
    assert result.tail.head == 2, "Second element should be the head of the tail of the first list"
    assert result.tail.tail.head == 3, "Third element should be the head of the second list"
    assert result.tail.tail.tail.head == 4, "Fourth element should be the head of the tail of the second list"

    # Test addition with non-ImmutableList should raise ValueError
    with pytest.raises(ValueError):
        result = list1 + [5, 6]

def test_immutable_list_addition_empty_tail():
    list1 = ImmutableList(1, None)
    list2 = ImmutableList(2, ImmutableList(3, None))

    # Test addition when the first ImmutableList has an empty tail
    result = list1 + list2
    assert isinstance(result, ImmutableList), "Result of addition should be an ImmutableList"
    assert result.head == 1, "Head of the result should be the head of the first list"
    assert result.tail.head == 2, "Second element should be the head of the second list"
    assert result.tail.tail.head == 3, "Third element should be the head of the tail of the second list"
