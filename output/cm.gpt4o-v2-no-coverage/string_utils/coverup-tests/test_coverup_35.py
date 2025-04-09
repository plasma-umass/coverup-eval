# file: string_utils/generation.py:88-140
# asked: {"lines": [88, 106, 107, 109, 110, 112, 113, 115, 116, 118, 119, 122, 123, 124, 127, 130, 131, 132, 135, 136, 137, 138, 140], "branches": [[109, 110], [109, 112], [112, 113], [112, 115], [115, 0], [115, 116], [122, 123], [122, 127], [137, 138], [137, 140]]}
# gained: {"lines": [88, 106, 107, 109, 112, 113, 115, 116, 118, 119, 122, 123, 124, 127, 130, 131, 132, 135, 136, 137, 138, 140], "branches": [[109, 112], [112, 113], [112, 115], [115, 0], [115, 116], [122, 123], [122, 127], [137, 138], [137, 140]]}

import pytest
from string_utils.generation import roman_range
from string_utils.manipulation import roman_encode

def test_roman_range_default():
    result = list(roman_range(7))
    expected = [roman_encode(i) for i in range(1, 8)]
    assert result == expected

def test_roman_range_custom_start():
    result = list(roman_range(7, start=3))
    expected = [roman_encode(i) for i in range(3, 8)]
    assert result == expected

def test_roman_range_custom_step():
    result = list(roman_range(7, start=1, step=2))
    expected = [roman_encode(i) for i in range(1, 8, 2)]
    assert result == expected

def test_roman_range_reverse():
    result = list(roman_range(1, start=7, step=-1))
    expected = [roman_encode(i) for i in range(7, 0, -1)]
    assert result == expected

def test_roman_range_invalid_start():
    with pytest.raises(ValueError):
        list(roman_range(7, start=4000))

def test_roman_range_invalid_stop():
    with pytest.raises(ValueError):
        list(roman_range(4000))

def test_roman_range_invalid_step():
    with pytest.raises(ValueError):
        list(roman_range(7, step=4000))

def test_roman_range_invalid_configuration():
    with pytest.raises(OverflowError):
        list(roman_range(1, start=7, step=1))

def test_roman_range_zero_step():
    with pytest.raises(ValueError):
        list(roman_range(7, step=0))
