# file pymonet/immutable_list.py:47-54
# lines [47, 48, 49, 51, 52, 54]
# branches ['48->49', '48->51', '51->52', '51->54']

import pytest
from pymonet.immutable_list import ImmutableList

class TestImmutableList:
    def test_len_with_empty_list(self):
        empty_list = ImmutableList()
        empty_list.head = None
        empty_list.tail = None
        assert len(empty_list) == 0

    def test_len_with_single_element_list(self):
        single_element_list = ImmutableList()
        single_element_list.head = 'head'
        single_element_list.tail = None
        assert len(single_element_list) == 1

    def test_len_with_multiple_elements_list(self, mocker):
        multiple_elements_list = ImmutableList()
        multiple_elements_list.head = 'head'
        mock_tail = mocker.Mock()
        mock_tail.__len__ = mocker.Mock(return_value=2)
        multiple_elements_list.tail = mock_tail
        assert len(multiple_elements_list) == 3
