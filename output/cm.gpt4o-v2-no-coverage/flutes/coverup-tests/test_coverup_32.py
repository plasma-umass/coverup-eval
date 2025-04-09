# file: flutes/iterator.py:258-261
# asked: {"lines": [260], "branches": [[259, 260]]}
# gained: {"lines": [260], "branches": [[259, 260]]}

import pytest
from typing import List

from flutes.iterator import LazyList

class TestLazyList:
    def test_iter_exhausted(self):
        data = [1, 2, 3]
        lazy_list = LazyList(data)
        lazy_list.exhausted = True
        lazy_list.list = data  # Manually set the list to the data
        result = list(iter(lazy_list))
        assert result == data

    def test_iter_not_exhausted(self, mocker):
        data = [1, 2, 3]
        lazy_list = LazyList(data)
        lazy_list.exhausted = False
        mock_iterator = mocker.patch.object(LazyList, 'LazyListIterator', autospec=True)
        iterator_instance = mock_iterator.return_value

        result = iter(lazy_list)
        assert result == iterator_instance
        mock_iterator.assert_called_once_with(lazy_list)
