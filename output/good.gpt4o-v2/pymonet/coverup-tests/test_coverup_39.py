# file: pymonet/utils.py:117-137
# asked: {"lines": [117, 132, 133, 134, 135, 137], "branches": [[133, 0], [133, 134], [134, 133], [134, 135]]}
# gained: {"lines": [117, 132, 133, 134, 135, 137], "branches": [[133, 0], [133, 134], [134, 133], [134, 135]]}

import pytest
from pymonet.utils import cond

def test_cond_first_condition_true():
    condition_list = [
        (lambda x: x > 0, lambda x: "positive"),
        (lambda x: x == 0, lambda x: "zero"),
        (lambda x: x < 0, lambda x: "negative")
    ]
    func = cond(condition_list)
    assert func(1) == "positive"

def test_cond_second_condition_true():
    condition_list = [
        (lambda x: x > 0, lambda x: "positive"),
        (lambda x: x == 0, lambda x: "zero"),
        (lambda x: x < 0, lambda x: "negative")
    ]
    func = cond(condition_list)
    assert func(0) == "zero"

def test_cond_third_condition_true():
    condition_list = [
        (lambda x: x > 0, lambda x: "positive"),
        (lambda x: x == 0, lambda x: "zero"),
        (lambda x: x < 0, lambda x: "negative")
    ]
    func = cond(condition_list)
    assert func(-1) == "negative"

def test_cond_no_condition_true():
    condition_list = [
        (lambda x: x > 1, lambda x: "greater than one"),
        (lambda x: x == 1, lambda x: "one")
    ]
    func = cond(condition_list)
    assert func(0) is None
