# file: pysnooper/utils.py:50-56
# asked: {"lines": [50, 51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [50, 51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

import pytest

from pysnooper.utils import get_repr_function

def test_get_repr_function_with_type_condition():
    custom_repr = [
        (int, lambda x: f"int: {x}"),
        (str, lambda x: f"str: {x}")
    ]
    item = 42
    repr_func = get_repr_function(item, custom_repr)
    assert repr_func(item) == "int: 42"

def test_get_repr_function_with_lambda_condition():
    custom_repr = [
        (lambda x: x == 42, lambda x: "The answer to life, the universe, and everything"),
        (str, lambda x: f"str: {x}")
    ]
    item = 42
    repr_func = get_repr_function(item, custom_repr)
    assert repr_func(item) == "The answer to life, the universe, and everything"

def test_get_repr_function_with_no_matching_condition():
    custom_repr = [
        (str, lambda x: f"str: {x}")
    ]
    item = 42
    repr_func = get_repr_function(item, custom_repr)
    assert repr_func(item) == repr(item)

def test_get_repr_function_with_multiple_conditions():
    custom_repr = [
        (int, lambda x: f"int: {x}"),
        (lambda x: x == 42, lambda x: "The answer to life, the universe, and everything"),
        (str, lambda x: f"str: {x}")
    ]
    item = 42
    repr_func = get_repr_function(item, custom_repr)
    assert repr_func(item) == "int: 42"
