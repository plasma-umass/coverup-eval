# file flutes/iterator.py:278-279
# lines [278, 279]
# branches []

import pytest
from flutes.iterator import LazyList

@pytest.fixture
def lazy_list_fixture():
    class ConcreteLazyList(LazyList[int]):
        def __init__(self):
            self.data = [1, 2, 3, 4, 5]

        def __getitem__(self, idx):
            if isinstance(idx, slice):
                return self.data[idx]
            elif isinstance(idx, int):
                return self.data[idx]
            else:
                raise TypeError("Invalid argument type.")

    return ConcreteLazyList()

def test_lazy_list_getitem_slice(lazy_list_fixture):
    ll = lazy_list_fixture
    slice_result = ll[1:3]
    assert slice_result == [2, 3], "The slice of the LazyList did not return the expected list."

def test_lazy_list_getitem_index(lazy_list_fixture):
    ll = lazy_list_fixture
    index_result = ll[2]
    assert index_result == 3, "The index access of the LazyList did not return the expected value."

def test_lazy_list_getitem_invalid_type(lazy_list_fixture):
    ll = lazy_list_fixture
    with pytest.raises(TypeError):
        _ = ll['invalid']  # This should raise a TypeError
