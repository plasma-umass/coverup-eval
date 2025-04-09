# file: pymonet/immutable_list.py:47-54
# asked: {"lines": [47, 48, 49, 51, 52, 54], "branches": [[48, 49], [48, 51], [51, 52], [51, 54]]}
# gained: {"lines": [47, 48, 49, 51, 52, 54], "branches": [[48, 49], [48, 51], [51, 52], [51, 54]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_len_with_empty_head():
    empty_list = ImmutableList()
    assert len(empty_list) == 0

def test_len_with_non_empty_head_and_empty_tail():
    single_element_list = ImmutableList(head=1)
    assert len(single_element_list) == 1

def test_len_with_non_empty_head_and_non_empty_tail():
    tail_list = ImmutableList(head=2)
    head_list = ImmutableList(head=1, tail=tail_list)
    assert len(head_list) == 2
