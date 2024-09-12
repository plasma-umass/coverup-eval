# file: f157/__init__.py:1-11
# asked: {"lines": [1, 11], "branches": []}
# gained: {"lines": [1, 11], "branches": []}

import pytest
from f157 import right_angle_triangle

def test_right_angle_triangle_true():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(6, 8, 10) == True

def test_right_angle_triangle_false():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 2, 2) == False
    assert right_angle_triangle(5, 5, 5) == False

def test_right_angle_triangle_unsorted():
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(13, 5, 12) == True
    assert right_angle_triangle(10, 6, 8) == True

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
