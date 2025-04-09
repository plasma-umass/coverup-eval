# file: flutes/iterator.py:92-111
# asked: {"lines": [92, 105, 106, 107, 108, 109, 110, 111], "branches": [[106, 107], [106, 111], [107, 108], [107, 109]]}
# gained: {"lines": [92, 105, 106, 107, 108, 109, 110, 111], "branches": [[106, 107], [106, 111], [107, 108], [107, 109]]}

import pytest
from flutes.iterator import drop_until

def test_drop_until_all_elements():
    result = list(drop_until(lambda x: x > 5, range(10)))
    assert result == [6, 7, 8, 9]

def test_drop_until_no_elements():
    result = list(drop_until(lambda x: x > 10, range(10)))
    assert result == []

def test_drop_until_first_element():
    result = list(drop_until(lambda x: x >= 0, range(10)))
    assert result == list(range(10))

def test_drop_until_middle_element():
    result = list(drop_until(lambda x: x >= 5, range(10)))
    assert result == [5, 6, 7, 8, 9]

def test_drop_until_empty_iterable():
    result = list(drop_until(lambda x: x > 5, []))
    assert result == []

def test_drop_until_non_integer_elements():
    result = list(drop_until(lambda x: x == 'b', ['a', 'b', 'c', 'd']))
    assert result == ['b', 'c', 'd']
