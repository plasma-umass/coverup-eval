# file: f041/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f041 import car_race_collision

def test_car_race_collision():
    # Test with a positive integer
    assert car_race_collision(2) == 4
    # Test with zero
    assert car_race_collision(0) == 0
    # Test with a negative integer
    assert car_race_collision(-3) == 9
