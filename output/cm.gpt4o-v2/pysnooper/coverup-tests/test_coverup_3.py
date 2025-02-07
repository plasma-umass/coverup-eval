# file: pysnooper/utils.py:50-56
# asked: {"lines": [50, 51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [50, 51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

import pytest
from pysnooper.utils import get_repr_function

def test_get_repr_function_with_type_condition():
    custom_repr = [(int, lambda x: f"int: {x}")]
    item = 5
    result = get_repr_function(item, custom_repr)
    assert result(item) == "int: 5"

def test_get_repr_function_with_lambda_condition():
    custom_repr = [(lambda x: x == 5, lambda x: f"five: {x}")]
    item = 5
    result = get_repr_function(item, custom_repr)
    assert result(item) == "five: 5"

def test_get_repr_function_no_match():
    custom_repr = [(lambda x: x == 10, lambda x: f"ten: {x}")]
    item = 5
    result = get_repr_function(item, custom_repr)
    assert result is repr
    assert result(item) == "5"
