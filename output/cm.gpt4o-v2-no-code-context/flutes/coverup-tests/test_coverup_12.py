# file: flutes/iterator.py:360-401
# asked: {"lines": [360, 361, 382, 383, 384, 386, 387, 389, 390, 392, 393, 394, 395, 397, 398, 400, 401], "branches": [[393, 394], [393, 395]]}
# gained: {"lines": [360, 361, 382, 383, 384, 386, 387, 389, 390, 392, 393, 394, 395, 397, 398, 400, 401], "branches": [[393, 394], [393, 395]]}

import pytest
from flutes.iterator import MapList

def test_maplist_getitem_int():
    lst = [1, 2, 3, 4, 5]
    map_list = MapList(lambda x: x * x, lst)
    assert map_list[2] == 9

def test_maplist_getitem_slice():
    lst = [1, 2, 3, 4, 5]
    map_list = MapList(lambda x: x * x, lst)
    assert map_list[1:4] == [4, 9, 16]

def test_maplist_iter():
    lst = [1, 2, 3, 4, 5]
    map_list = MapList(lambda x: x * x, lst)
    assert list(map_list) == [1, 4, 9, 16, 25]

def test_maplist_len():
    lst = [1, 2, 3, 4, 5]
    map_list = MapList(lambda x: x * x, lst)
    assert len(map_list) == 5
