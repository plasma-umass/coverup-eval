# file flutes/iterator.py:360-401
# lines [360, 361, 382, 383, 384, 386, 387, 389, 390, 392, 393, 394, 395, 397, 398, 400, 401]
# branches ['393->394', '393->395']

import pytest
from flutes.iterator import MapList

def test_maplist():
    # Test __getitem__ with an integer index
    lst = [1, 2, 3, 4, 5]
    map_list = MapList(lambda x: x * x, lst)
    assert map_list[2] == 9  # 3 * 3

    # Test __getitem__ with a slice
    assert map_list[1:4] == [4, 9, 16]  # [2*2, 3*3, 4*4]

    # Test __iter__
    iterated = list(iter(map_list))
    assert iterated == [1, 4, 9, 16, 25]  # [1*1, 2*2, 3*3, 4*4, 5*5]

    # Test __len__
    assert len(map_list) == 5

    # Test with a different function and list
    lst2 = [2, 3, 4, 5, 6]
    map_list2 = MapList(lambda x: x + 1, lst2)
    assert map_list2[0] == 3  # 2 + 1
    assert map_list2[1:3] == [4, 5]  # [3+1, 4+1]
    assert list(iter(map_list2)) == [3, 4, 5, 6, 7]  # [2+1, 3+1, 4+1, 5+1, 6+1]
    assert len(map_list2) == 5

    # Test with a more complex function
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    map_list3 = MapList(lambda i: a[i] * b[i], range(len(a)))
    assert map_list3[0] == 2  # 1 * 2
    assert map_list3[1:3] == [6, 12]  # [2*3, 3*4]
    assert list(iter(map_list3)) == [2, 6, 12, 20, 30]  # [1*2, 2*3, 3*4, 4*5, 5*6]
    assert len(map_list3) == 5
