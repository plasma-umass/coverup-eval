# file pymonet/immutable_list.py:47-54
# lines [47, 48, 49, 51, 52, 54]
# branches ['48->49', '48->51', '51->52', '51->54']

import pytest
from pymonet.immutable_list import ImmutableList

class TestImmutableList:

    def test_immutable_list_len(self):
        # Test the case where head is None
        empty_list = ImmutableList()
        empty_list.head = None
        assert len(empty_list) == 0

        # Test the case where tail is None
        single_item_list = ImmutableList()
        single_item_list.head = 'a'
        single_item_list.tail = None
        assert len(single_item_list) == 1

        # Test the case where tail is not None
        multi_item_list = ImmutableList()
        multi_item_list.head = 'a'
        tail_list = ImmutableList()
        tail_list.head = 'b'
        tail_list.tail = None
        multi_item_list.tail = tail_list
        assert len(multi_item_list) == 2
