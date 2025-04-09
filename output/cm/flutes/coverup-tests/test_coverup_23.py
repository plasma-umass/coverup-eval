# file flutes/iterator.py:258-261
# lines [258, 259, 260, 261]
# branches ['259->260', '259->261']

import pytest
from flutes.iterator import LazyList

class MockIterable:
    def __iter__(self):
        return iter([1, 2, 3])

@pytest.fixture
def lazy_list_fixture():
    mock_iterable = MockIterable()
    lazy_list = LazyList(mock_iterable)
    lazy_list.exhausted = False
    lazy_list.list = [1, 2, 3]
    yield lazy_list
    # No cleanup needed as the lazy_list is a local variable and will be garbage collected

def test_lazy_list_iterator_exhausted(lazy_list_fixture):
    lazy_list_fixture.exhausted = True
    iterator = iter(lazy_list_fixture)
    assert list(iterator) == [1, 2, 3]

def test_lazy_list_iterator_not_exhausted(mocker, lazy_list_fixture):
    lazy_list_fixture.exhausted = False
    lazy_list_iterator_mock = mocker.patch.object(lazy_list_fixture, 'LazyListIterator', return_value=iter([4, 5, 6]))
    iterator = iter(lazy_list_fixture)
    assert list(iterator) == [4, 5, 6]
    lazy_list_iterator_mock.assert_called_once_with(lazy_list_fixture)
