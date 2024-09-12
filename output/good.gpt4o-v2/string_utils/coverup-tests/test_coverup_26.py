# file: string_utils/generation.py:88-140
# asked: {"lines": [88, 106, 107, 109, 110, 112, 113, 115, 116, 118, 119, 122, 123, 124, 127, 130, 131, 132, 135, 136, 137, 138, 140], "branches": [[109, 110], [109, 112], [112, 113], [112, 115], [115, 0], [115, 116], [122, 123], [122, 127], [137, 138], [137, 140]]}
# gained: {"lines": [88, 106, 107, 109, 112, 113, 115, 116, 118, 119, 122, 123, 124, 127, 130, 131, 132, 135, 136, 137, 138, 140], "branches": [[109, 112], [112, 113], [112, 115], [115, 0], [115, 116], [122, 123], [122, 127], [137, 138], [137, 140]]}

import pytest
from string_utils.generation import roman_range

def test_roman_range_default():
    result = list(roman_range(7))
    assert result == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

def test_roman_range_custom_start_stop_step():
    result = list(roman_range(start=7, stop=1, step=-1))
    assert result == ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']

def test_roman_range_invalid_start():
    with pytest.raises(ValueError, match='"start" must be an integer in the range 1-3999'):
        list(roman_range(start=0, stop=10))

def test_roman_range_invalid_stop():
    with pytest.raises(ValueError, match='"stop" must be an integer in the range 1-3999'):
        list(roman_range(stop=4000))

def test_roman_range_invalid_step():
    with pytest.raises(ValueError, match='"step" must be an integer in the range 1-3999'):
        list(roman_range(start=1, stop=10, step=0))

def test_roman_range_invalid_configuration_forward():
    with pytest.raises(OverflowError, match='Invalid start/stop/step configuration'):
        list(roman_range(start=10, stop=1, step=1))

def test_roman_range_invalid_configuration_backward():
    with pytest.raises(OverflowError, match='Invalid start/stop/step configuration'):
        list(roman_range(start=1, stop=10, step=-1))
