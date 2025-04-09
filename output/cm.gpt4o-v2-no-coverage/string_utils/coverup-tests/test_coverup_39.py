# file: string_utils/manipulation.py:52-76
# asked: {"lines": [52, 53, 55, 56, 59, 60, 63, 64, 67, 68, 71, 72, 73, 76], "branches": [[55, 56], [55, 59], [59, 60], [59, 63], [63, 64], [63, 67], [67, 68], [67, 71], [71, 72], [71, 76]]}
# gained: {"lines": [52, 53, 55, 56, 59, 60, 63, 64, 67, 68, 71, 72, 73, 76], "branches": [[55, 56], [55, 59], [59, 60], [59, 63], [63, 64], [63, 67], [67, 68], [67, 71], [71, 72], [71, 76]]}

import pytest
from string_utils.manipulation import __RomanNumbers

@pytest.mark.parametrize("index, value, expected", [
    (0, 0, ''),
    (0, 1, 'I'),
    (0, 2, 'II'),
    (0, 3, 'III'),
    (0, 4, 'IV'),
    (0, 5, 'V'),
    (0, 6, 'VI'),
    (0, 7, 'VII'),
    (0, 8, 'VIII'),
    (0, 9, 'IX'),
    (1, 0, ''),
    (1, 1, 'X'),
    (1, 2, 'XX'),
    (1, 3, 'XXX'),
    (1, 4, 'XL'),
    (1, 5, 'L'),
    (1, 6, 'LX'),
    (1, 7, 'LXX'),
    (1, 8, 'LXXX'),
    (1, 9, 'XC'),
])
def test_encode_digit(index, value, expected):
    result = __RomanNumbers._RomanNumbers__encode_digit(index, value)
    assert result == expected
