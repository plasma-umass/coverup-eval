# file: f071/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import pytest
from f071 import triangle_area

def test_triangle_area_valid_triangle():
    assert triangle_area(3, 4, 5) == 6.0

def test_triangle_area_invalid_triangle():
    assert triangle_area(1, 1, 3) == -1
    assert triangle_area(1, 3, 1) == -1
    assert triangle_area(3, 1, 1) == -1

def test_triangle_area_cleanup():
    # No state to clean up in this case
    assert triangle_area(3, 4, 5) == 6.0
