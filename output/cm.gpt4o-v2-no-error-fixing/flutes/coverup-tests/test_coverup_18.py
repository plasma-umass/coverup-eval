# file: flutes/iterator.py:47-66
# asked: {"lines": [47, 59, 60, 61, 62, 63, 64, 65, 66], "branches": [[59, 60], [59, 61], [63, 0], [63, 64]]}
# gained: {"lines": [47, 59, 60, 61, 62, 63, 64, 65, 66], "branches": [[59, 60], [59, 61], [63, 0], [63, 64]]}

import pytest
from flutes.iterator import take

def test_take_with_positive_n():
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]

def test_take_with_zero_n():
    result = list(take(0, range(10)))
    assert result == []

def test_take_with_negative_n():
    with pytest.raises(ValueError, match="`n` should be non-negative"):
        list(take(-1, range(10)))

def test_take_with_exhausted_iterable():
    result = list(take(5, range(3)))
    assert result == [0, 1, 2]

def test_take_with_empty_iterable():
    result = list(take(5, iter([])))
    assert result == []

@pytest.fixture
def mock_iterable(mocker):
    mock = mocker.Mock()
    mock.__iter__ = mocker.Mock(return_value=iter([1, 2, 3]))
    return mock

def test_take_with_mocked_iterable(mock_iterable):
    result = list(take(2, mock_iterable))
    assert result == [1, 2]
