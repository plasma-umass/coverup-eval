# file: string_utils/generation.py:88-140
# asked: {"lines": [110], "branches": [[109, 110]]}
# gained: {"lines": [110], "branches": [[109, 110]]}

import pytest
from string_utils.generation import roman_range

def test_roman_range_invalid_type():
    with pytest.raises(ValueError, match='"stop" must be an integer in the range 1-3999'):
        list(roman_range("10"))

    with pytest.raises(ValueError, match='"start" must be an integer in the range 1-3999'):
        list(roman_range(10, "1"))

    with pytest.raises(ValueError, match='"step" must be an integer in the range 1-3999'):
        list(roman_range(10, 1, "1"))

def test_roman_range_invalid_value():
    with pytest.raises(ValueError, match='"stop" must be an integer in the range 1-3999'):
        list(roman_range(4000))

    with pytest.raises(ValueError, match='"start" must be an integer in the range 1-3999'):
        list(roman_range(10, 0))

    with pytest.raises(ValueError, match='"step" must be an integer in the range 1-3999'):
        list(roman_range(10, 1, 0))

def test_roman_range_overflow():
    with pytest.raises(OverflowError, match='Invalid start/stop/step configuration'):
        list(roman_range(1, 10))

    with pytest.raises(OverflowError, match='Invalid start/stop/step configuration'):
        list(roman_range(10, 1, -1))

    with pytest.raises(OverflowError, match='Invalid start/stop/step configuration'):
        list(roman_range(1, 10, 2))

    with pytest.raises(OverflowError, match='Invalid start/stop/step configuration'):
        list(roman_range(10, 1, -2))

def test_roman_range_valid():
    assert list(roman_range(7)) == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    assert list(roman_range(7, 1, 2)) == ['I', 'III', 'V', 'VII']
    assert list(roman_range(7, 1, 3)) == ['I', 'IV', 'VII']
    assert list(roman_range(1, 7, -1)) == ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
    assert list(roman_range(1, 7, -2)) == ['VII', 'V', 'III', 'I']
