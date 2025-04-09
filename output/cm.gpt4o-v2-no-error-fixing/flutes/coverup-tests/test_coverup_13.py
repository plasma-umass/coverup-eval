# file: flutes/iterator.py:124-157
# asked: {"lines": [124, 144, 145, 146, 147, 148, 149, 150, 151, 153, 154, 155, 156, 157], "branches": [[144, 145], [144, 146], [146, 147], [146, 148], [149, 150], [149, 156], [150, 151], [150, 153], [153, 154], [153, 155], [156, 0], [156, 157]]}
# gained: {"lines": [124, 144, 145, 146, 147, 148, 149, 150, 151, 153, 154, 155, 156, 157], "branches": [[144, 145], [144, 146], [146, 147], [146, 148], [149, 150], [149, 156], [150, 151], [150, 153], [153, 154], [153, 155], [156, 0], [156, 157]]}

import pytest
from flutes.iterator import split_by

def test_split_by_with_criterion():
    iterable = range(10)
    criterion = lambda x: x % 3 == 0
    result = list(split_by(iterable, criterion=criterion))
    assert result == [[1, 2], [4, 5], [7, 8]]

def test_split_by_with_separator():
    iterable = " Split by: "
    separator = ' '
    result = list(split_by(iterable, empty_segments=True, separator=separator))
    assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

def test_split_by_empty_segments_false():
    iterable = " Split by: "
    separator = ' '
    result = list(split_by(iterable, empty_segments=False, separator=separator))
    assert result == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]

def test_split_by_invalid_arguments():
    iterable = range(10)
    with pytest.raises(ValueError, match="Exactly one of `criterion` and `separator` should be specified"):
        list(split_by(iterable))

    with pytest.raises(ValueError, match="Exactly one of `criterion` and `separator` should be specified"):
        list(split_by(iterable, criterion=lambda x: x % 3 == 0, separator=3))
