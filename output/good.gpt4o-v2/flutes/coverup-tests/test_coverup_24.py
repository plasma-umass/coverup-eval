# file: flutes/iterator.py:258-261
# asked: {"lines": [258, 259, 260, 261], "branches": [[259, 260], [259, 261]]}
# gained: {"lines": [258, 259, 260, 261], "branches": [[259, 260], [259, 261]]}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_iter_exhausted():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    lazy_list.list = data  # Manually set the internal list to the data
    lazy_list.exhausted = True  # Force the list to be marked as exhausted
    iterator = iter(lazy_list)
    assert list(iterator) == data  # Verify that the iterator returns the full list

def test_lazy_list_iter_not_exhausted(mocker):
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    lazy_list_iterator_mock = mocker.patch.object(LazyList, 'LazyListIterator', autospec=True)
    iterator = iter(lazy_list)
    lazy_list_iterator_mock.assert_called_once_with(lazy_list)  # Verify that LazyListIterator is called
