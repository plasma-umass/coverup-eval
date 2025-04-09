# file: flutes/iterator.py:258-261
# asked: {"lines": [258, 259, 260, 261], "branches": [[259, 260], [259, 261]]}
# gained: {"lines": [258, 259, 260, 261], "branches": [[259, 260], [259, 261]]}

import pytest
from flutes.iterator import LazyList

def test_lazylist_iter_exhausted():
    mock_list = [1, 2, 3]
    lazy_list = LazyList(mock_list)
    lazy_list.exhausted = True
    lazy_list.list = mock_list

    result = list(iter(lazy_list))
    assert result == mock_list

def test_lazylist_iter_not_exhausted():
    mock_list = [1, 2, 3]
    lazy_list = LazyList(mock_list)
    lazy_list.exhausted = False

    result = iter(lazy_list)
    assert isinstance(result, LazyList.LazyListIterator)
    assert result.list() == lazy_list
