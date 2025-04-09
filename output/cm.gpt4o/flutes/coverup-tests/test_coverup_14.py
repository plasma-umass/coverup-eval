# file flutes/iterator.py:124-157
# lines [124, 144, 145, 146, 147, 148, 149, 150, 151, 153, 154, 155, 156, 157]
# branches ['144->145', '144->146', '146->147', '146->148', '149->150', '149->156', '150->151', '150->153', '153->154', '153->155', '156->exit', '156->157']

import pytest
from flutes.iterator import split_by

def test_split_by_criterion():
    # Test with criterion
    result = list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8]], f"Unexpected result: {result}"

def test_split_by_separator():
    # Test with separator
    result = list(split_by(" Split by: ", empty_segments=True, separator=' '))
    assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []], f"Unexpected result: {result}"

def test_split_by_empty_segments_false():
    # Test with empty_segments=False
    result = list(split_by(" Split by: ", empty_segments=False, separator=' '))
    assert result == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']], f"Unexpected result: {result}"

def test_split_by_empty_segments_true():
    # Test with empty_segments=True
    result = list(split_by(" Split by: ", empty_segments=True, separator=' '))
    assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []], f"Unexpected result: {result}"

def test_split_by_invalid_arguments():
    # Test with invalid arguments
    with pytest.raises(ValueError, match="Exactly one of `criterion` and `separator` should be specified"):
        list(split_by(range(10), criterion=lambda x: x % 3 == 0, separator=3))

    with pytest.raises(ValueError, match="Exactly one of `criterion` and `separator` should be specified"):
        list(split_by(range(10)))

def test_split_by_no_criterion_no_separator():
    # Test with no criterion and no separator
    with pytest.raises(ValueError, match="Exactly one of `criterion` and `separator` should be specified"):
        list(split_by(range(10)))

def test_split_by_only_separator():
    # Test with only separator
    result = list(split_by(" Split by: ", separator=' '))
    assert result == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']], f"Unexpected result: {result}"

def test_split_by_only_criterion():
    # Test with only criterion
    result = list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8]], f"Unexpected result: {result}"
