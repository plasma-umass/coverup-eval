# file: f109/__init__.py:1-14
# asked: {"lines": [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest
from f109 import move_one_ball

def test_move_one_ball_empty_array():
    assert move_one_ball([]) == True

def test_move_one_ball_sorted_array():
    assert move_one_ball([1, 2, 3, 4, 5]) == True

def test_move_one_ball_unsorted_array():
    assert move_one_ball([3, 1, 2, 5, 4]) == False

def test_move_one_ball_single_element():
    assert move_one_ball([1]) == True

def test_move_one_ball_reverse_sorted_array():
    assert move_one_ball([5, 4, 3, 2, 1]) == False

def test_move_one_ball_rotated_sorted_array():
    assert move_one_ball([3, 4, 5, 1, 2]) == True
