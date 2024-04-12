# file flutes/iterator.py:69-89
# lines [69, 81, 82, 83, 84, 85, 86, 87, 88, 89]
# branches ['81->82', '81->83', '85->86', '85->87']

import pytest
from flutes.iterator import drop

def test_drop():
    # Test dropping elements from a range
    result = list(drop(5, range(10)))
    assert result == [5, 6, 7, 8, 9], "Dropping the first 5 elements from range(10) should yield [5, 6, 7, 8, 9]"

    # Test dropping more elements than the iterable has
    result = list(drop(15, range(10)))
    assert result == [], "Dropping more elements than the iterable has should yield an empty list"

    # Test dropping elements from an empty iterable
    result = list(drop(5, []))
    assert result == [], "Dropping elements from an empty iterable should yield an empty list"

    # Test dropping zero elements
    result = list(drop(0, range(10)))
    assert result == list(range(10)), "Dropping zero elements should yield the original iterable"

    # Test dropping a negative number of elements (should raise ValueError)
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))

def test_drop_with_mock(mocker):
    # Mock an iterable to test the StopIteration branch
    mock_iterable = mocker.MagicMock()
    mock_iterator = mocker.MagicMock()
    mock_iterable.__iter__.return_value = mock_iterator
    mock_iterator.__next__.side_effect = StopIteration

    result = list(drop(5, mock_iterable))
    assert result == [], "Dropping elements from an iterable that raises StopIteration should yield an empty list"
