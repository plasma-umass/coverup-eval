# file: flutes/iterator.py:124-157
# asked: {"lines": [124, 144, 145, 146, 147, 148, 149, 150, 151, 153, 154, 155, 156, 157], "branches": [[144, 145], [144, 146], [146, 147], [146, 148], [149, 150], [149, 156], [150, 151], [150, 153], [153, 154], [153, 155], [156, 0], [156, 157]]}
# gained: {"lines": [124, 144, 145, 146, 147, 148, 149, 150, 151, 153, 154, 155, 156, 157], "branches": [[144, 145], [144, 146], [146, 147], [146, 148], [149, 150], [149, 156], [150, 151], [150, 153], [153, 154], [153, 155], [156, 0], [156, 157]]}

import pytest
from flutes.iterator import split_by

def test_split_by_criterion():
    result = list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8]]

def test_split_by_separator():
    result = list(split_by(" Split by: ", empty_segments=True, separator=' '))
    assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

def test_split_by_empty_segments_false():
    result = list(split_by(" Split by: ", empty_segments=False, separator=' '))
    assert result == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]

def test_split_by_invalid_arguments():
    with pytest.raises(ValueError, match="Exactly one of `criterion` and `separator` should be specified"):
        list(split_by(" Split by: ", criterion=lambda x: x == ' ', separator=' '))

def test_split_by_no_criterion_or_separator():
    with pytest.raises(ValueError, match="Exactly one of `criterion` and `separator` should be specified"):
        list(split_by(" Split by: "))

def test_split_by_empty_iterable():
    result = list(split_by("", empty_segments=True, separator=' '))
    assert result == [[]]

def test_split_by_no_empty_segments():
    result = list(split_by("Splitby:", empty_segments=False, separator=' '))
    assert result == [['S', 'p', 'l', 'i', 't', 'b', 'y', ':']]

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup code before each test
    yield
    # Teardown code after each test
    # No specific teardown needed for these tests
