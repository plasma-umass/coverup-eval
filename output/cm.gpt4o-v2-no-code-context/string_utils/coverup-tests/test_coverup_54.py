# file: string_utils/generation.py:88-140
# asked: {"lines": [110], "branches": [[109, 110]]}
# gained: {"lines": [110], "branches": [[109, 110]]}

import pytest
from string_utils.generation import roman_range

def test_roman_range_invalid_stop_type():
    with pytest.raises(ValueError, match='"stop" must be an integer in the range 1-3999'):
        list(roman_range("VII"))

def test_roman_range_invalid_start_type():
    with pytest.raises(ValueError, match='"start" must be an integer in the range 1-3999'):
        list(roman_range(10, start="I"))

def test_roman_range_invalid_step_type():
    with pytest.raises(ValueError, match='"step" must be an integer in the range 1-3999'):
        list(roman_range(10, step="I"))

def test_roman_range_invalid_stop_value():
    with pytest.raises(ValueError, match='"stop" must be an integer in the range 1-3999'):
        list(roman_range(4000))

def test_roman_range_invalid_start_value():
    with pytest.raises(ValueError, match='"start" must be an integer in the range 1-3999'):
        list(roman_range(10, start=0))

def test_roman_range_invalid_step_value():
    with pytest.raises(ValueError, match='"step" must be an integer in the range 1-3999'):
        list(roman_range(10, step=4000))

def test_roman_range_invalid_step_zero():
    with pytest.raises(ValueError, match='"step" must be an integer in the range 1-3999'):
        list(roman_range(10, step=0))

def test_roman_range_overflow_forward():
    with pytest.raises(OverflowError, match='Invalid start/stop/step configuration'):
        list(roman_range(1, start=10, step=1))

def test_roman_range_overflow_backward():
    with pytest.raises(OverflowError, match='Invalid start/stop/step configuration'):
        list(roman_range(10, start=1, step=-1))

def test_roman_range_valid():
    result = list(roman_range(7))
    assert result == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

def test_roman_range_valid_reverse():
    result = list(roman_range(start=7, stop=1, step=-1))
    assert result == ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
