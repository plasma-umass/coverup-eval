# file: pymonet/utils.py:117-137
# asked: {"lines": [117, 132, 133, 134, 135, 137], "branches": [[133, 0], [133, 134], [134, 133], [134, 135]]}
# gained: {"lines": [117, 132, 133, 134, 135, 137], "branches": [[133, 0], [133, 134], [134, 133], [134, 135]]}

import pytest
from typing import List, Tuple, Callable

# Assuming the cond function is imported from pymonet.utils
from pymonet.utils import cond

def test_cond_all_conditions_false():
    condition_list = [
        (lambda x: x > 10, lambda x: "greater than 10"),
        (lambda x: x < 0, lambda x: "less than 0")
    ]
    func = cond(condition_list)
    assert func(5) is None

def test_cond_first_condition_true():
    condition_list = [
        (lambda x: x > 10, lambda x: "greater than 10"),
        (lambda x: x < 0, lambda x: "less than 0")
    ]
    func = cond(condition_list)
    assert func(15) == "greater than 10"

def test_cond_second_condition_true():
    condition_list = [
        (lambda x: x > 10, lambda x: "greater than 10"),
        (lambda x: x < 0, lambda x: "less than 0")
    ]
    func = cond(condition_list)
    assert func(-5) == "less than 0"

def test_cond_no_conditions():
    condition_list = []
    func = cond(condition_list)
    assert func(5) is None

def test_cond_multiple_conditions():
    condition_list = [
        (lambda x: x == 0, lambda x: "zero"),
        (lambda x: x > 0, lambda x: "positive"),
        (lambda x: x < 0, lambda x: "negative")
    ]
    func = cond(condition_list)
    assert func(0) == "zero"
    assert func(10) == "positive"
    assert func(-10) == "negative"
