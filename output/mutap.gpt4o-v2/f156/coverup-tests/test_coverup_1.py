# file: f156/__init__.py:1-16
# asked: {"lines": [1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest
from f156 import int_to_mini_roman

def test_int_to_mini_roman():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(58) == 'lviii'
    assert int_to_mini_roman(1994) == 'mcmxciv'
