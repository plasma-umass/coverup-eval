# file flutes/iterator.py:263-273
# lines [263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273]
# branches ['264->265', '264->266', '267->268', '267->269', '269->exit', '269->270']

import pytest
from flutes.iterator import LazyList

def test_lazy_list_fetch_until():
    # Mocking an iterator that will raise StopIteration after 3 elements
    mock_iter = iter([1, 2, 3])

    # Creating a LazyList instance with the mocked iterator
    lazy_list = LazyList(mock_iter)

    # Fetching until a specific index to ensure the while loop runs
    lazy_list._fetch_until(2)
    assert len(lazy_list.list) == 3
    assert lazy_list.exhausted is False

    # Fetching with a negative index to hit the line where idx is set to None
    lazy_list._fetch_until(-1)
    assert len(lazy_list.list) == 3  # No change expected, as the list is already populated

    # Fetching with None to simulate an unbounded fetch and trigger StopIteration
    lazy_list._fetch_until(None)
    assert lazy_list.exhausted is True
    with pytest.raises(AttributeError):
        _ = lazy_list.iter  # iter should be deleted after exhaustion

    # Fetching again after the list is exhausted to ensure early return
    lazy_list._fetch_until(0)  # No action should be taken, as the list is already exhausted
    assert len(lazy_list.list) == 3  # No change expected
    assert lazy_list.exhausted is True
