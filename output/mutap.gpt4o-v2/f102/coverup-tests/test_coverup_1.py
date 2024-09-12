# file: f102/__init__.py:1-9
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest
from f102 import choose_num

def test_choose_num_x_greater_than_y():
    assert choose_num(5, 3) == -1

def test_choose_num_y_even():
    assert choose_num(2, 4) == 4

def test_choose_num_x_equals_y():
    assert choose_num(3, 3) == -1

def test_choose_num_y_odd():
    assert choose_num(2, 5) == 4
