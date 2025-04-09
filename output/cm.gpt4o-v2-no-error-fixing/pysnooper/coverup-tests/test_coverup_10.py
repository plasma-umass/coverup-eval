# file: pysnooper/utils.py:50-56
# asked: {"lines": [50, 51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [50, 51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

import pytest
from pysnooper.utils import get_repr_function

def test_get_repr_function_with_type_condition():
    class CustomClass:
        pass

    def custom_action(x):
        return f"Custom action for {x}"

    custom_repr = [(CustomClass, custom_action)]
    item = CustomClass()
    result = get_repr_function(item, custom_repr)
    assert result == custom_action

def test_get_repr_function_with_lambda_condition():
    def custom_action(x):
        return f"Custom action for {x}"

    custom_repr = [(lambda x: isinstance(x, int), custom_action)]
    item = 42
    result = get_repr_function(item, custom_repr)
    assert result == custom_action

def test_get_repr_function_no_match():
    def custom_action(x):
        return f"Custom action for {x}"

    custom_repr = [(lambda x: isinstance(x, int), custom_action)]
    item = "string"
    result = get_repr_function(item, custom_repr)
    assert result == repr
