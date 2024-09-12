# file: f099/__init__.py:1-21
# asked: {"lines": [1, 3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [1, 3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17]]}

import pytest
from f099 import closest_integer

def test_closest_integer_with_decimal_and_trailing_zeros():
    assert closest_integer("123.4500") == 123

def test_closest_integer_with_positive_half():
    assert closest_integer("123.5") == 124

def test_closest_integer_with_negative_half():
    assert closest_integer("-123.5") == -124

def test_closest_integer_with_no_decimal():
    assert closest_integer("123") == 123

def test_closest_integer_with_zero():
    assert closest_integer("0") == 0

def test_closest_integer_with_empty_string():
    with pytest.raises(ValueError):
        closest_integer("")
