# file: f150/__init__.py:1-10
# asked: {"lines": [1, 3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

import pytest
from f150 import x_or_y

def test_x_or_y_n_equals_1():
    assert x_or_y(1, 'x', 'y') == 'y'

def test_x_or_y_n_is_composite():
    assert x_or_y(4, 'x', 'y') == 'y'

def test_x_or_y_n_is_prime():
    assert x_or_y(5, 'x', 'y') == 'x'
