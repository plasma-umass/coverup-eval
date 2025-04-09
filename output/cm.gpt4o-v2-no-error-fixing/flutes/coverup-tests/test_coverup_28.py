# file: flutes/iterator.py:288-292
# asked: {"lines": [289, 290, 292], "branches": [[289, 290], [289, 292]]}
# gained: {"lines": [289, 290, 292], "branches": [[289, 290], [289, 292]]}

import pytest
from typing import List

from flutes.iterator import LazyList

def test_len_exhausted():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    # Exhaust the iterator
    for _ in lazy_list:
        pass
    
    assert lazy_list.exhausted == True
    assert len(lazy_list) == len(data)

def test_len_not_exhausted():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    with pytest.raises(TypeError, match="__len__ is not available before the iterable is depleted"):
        len(lazy_list)
