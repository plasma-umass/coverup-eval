# file: flutes/iterator.py:360-401
# asked: {"lines": [383, 384, 393, 394, 395, 398, 401], "branches": [[393, 394], [393, 395]]}
# gained: {"lines": [383, 384, 393, 394, 395, 398, 401], "branches": [[393, 394], [393, 395]]}

import pytest
from typing import List

from flutes.iterator import MapList

def test_maplist_init():
    func = lambda x: x * 2
    lst = [1, 2, 3]
    map_list = MapList(func, lst)
    assert map_list.func == func
    assert map_list.list == lst

def test_maplist_getitem_int():
    func = lambda x: x * 2
    lst = [1, 2, 3]
    map_list = MapList(func, lst)
    assert map_list[1] == 4

def test_maplist_getitem_slice():
    func = lambda x: x * 2
    lst = [1, 2, 3]
    map_list = MapList(func, lst)
    assert map_list[0:2] == [2, 4]

def test_maplist_iter():
    func = lambda x: x * 2
    lst = [1, 2, 3]
    map_list = MapList(func, lst)
    assert list(iter(map_list)) == [2, 4, 6]

def test_maplist_len():
    lst = [1, 2, 3]
    map_list = MapList(lambda x: x, lst)
    assert len(map_list) == 3
