# file: httpie/context.py:122-124
# asked: {"lines": [122, 123, 124], "branches": []}
# gained: {"lines": [122, 123, 124], "branches": []}

import pytest
from httpie.context import Environment

def test_devnull_setter():
    env = Environment()
    dummy_value = "dummy_value"
    env.devnull = dummy_value
    assert env._devnull == dummy_value
