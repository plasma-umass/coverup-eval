# file flutes/iterator.py:288-292
# lines [288, 289, 290, 292]
# branches ['289->290', '289->292']

import pytest
from flutes.iterator import LazyList

class MockIterable:
    def __iter__(self):
        return iter([1, 2, 3])

@pytest.fixture
def mock_exhausted_lazy_list():
    lazy_list = LazyList(MockIterable())
    lazy_list.exhausted = True
    lazy_list.list = [1, 2, 3]
    return lazy_list

@pytest.fixture
def mock_non_exhausted_lazy_list():
    lazy_list = LazyList(MockIterable())
    lazy_list.exhausted = False
    return lazy_list

def test_len_on_exhausted_lazy_list(mock_exhausted_lazy_list):
    assert len(mock_exhausted_lazy_list) == 3

def test_len_on_non_exhausted_lazy_list_raises(mock_non_exhausted_lazy_list):
    with pytest.raises(TypeError) as exc_info:
        len(mock_non_exhausted_lazy_list)
    assert "__len__ is not available before the iterable is depleted" in str(exc_info.value)
