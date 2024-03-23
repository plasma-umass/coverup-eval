# file flutes/iterator.py:124-157
# lines [145]
# branches ['144->145', '146->148', '153->155']

import pytest
from flutes.iterator import split_by

def test_split_by_coverage():
    # Test the case where both criterion and separator are None
    with pytest.raises(ValueError):
        next(split_by(range(10)))

    # Test the case where criterion is None and separator is provided
    result = list(split_by(" Split by: ", empty_segments=True, separator=' '))
    assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

    # Test the case where criterion is provided and separator is None
    result = list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8]]

    # Test the case where empty_segments is False and the last segment is empty
    result = list(split_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3], criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8], [10]]

    # Test the case where empty_segments is True and the last segment is empty
    result = list(split_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3], empty_segments=True, criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8], [10], []]
