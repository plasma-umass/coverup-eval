# file: flutes/iterator.py:288-292
# asked: {"lines": [288, 289, 290, 292], "branches": [[289, 290], [289, 292]]}
# gained: {"lines": [288, 289, 290, 292], "branches": [[289, 290], [289, 292]]}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_len_exhausted():
    lazy_list = LazyList([1, 2, 3])
    lazy_list.exhausted = True
    lazy_list.list = [1, 2, 3]
    assert len(lazy_list) == 3

def test_lazy_list_len_not_exhausted():
    lazy_list = LazyList([1, 2, 3])
    lazy_list.exhausted = False
    with pytest.raises(TypeError, match="__len__ is not available before the iterable is depleted"):
        len(lazy_list)
