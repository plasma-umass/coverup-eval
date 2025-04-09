# file: flutes/iterator.py:69-89
# asked: {"lines": [69, 81, 82, 83, 84, 85, 86, 87, 88, 89], "branches": [[81, 82], [81, 83], [85, 86], [85, 87]]}
# gained: {"lines": [69, 81, 82, 83, 84, 85, 86, 87, 88, 89], "branches": [[81, 82], [81, 83], [85, 86], [85, 87]]}

import pytest
from typing import Iterable, Iterator
from flutes.iterator import drop

def test_drop_positive_n():
    result = list(drop(3, range(10)))
    assert result == [3, 4, 5, 6, 7, 8, 9]

def test_drop_zero_n():
    result = list(drop(0, range(5)))
    assert result == [0, 1, 2, 3, 4]

def test_drop_n_greater_than_iterable():
    result = list(drop(10, range(5)))
    assert result == []

def test_drop_negative_n():
    with pytest.raises(ValueError, match="`n` should be non-negative"):
        list(drop(-1, range(5)))

def test_drop_empty_iterable():
    result = list(drop(3, []))
    assert result == []

def test_drop_stop_iteration():
    def limited_iterable():
        yield 1
        yield 2
    result = list(drop(3, limited_iterable()))
    assert result == []

@pytest.fixture
def mock_iterable(mocker):
    return mocker.patch('flutes.iterator.iter')

def test_drop_iter_called(mock_iterable):
    iterable = range(5)
    list(drop(2, iterable))
    mock_iterable.assert_called_once_with(iterable)
