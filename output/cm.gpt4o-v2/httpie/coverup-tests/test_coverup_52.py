# file: httpie/context.py:122-124
# asked: {"lines": [122, 123, 124], "branches": []}
# gained: {"lines": [122, 123, 124], "branches": []}

import pytest
from httpie.context import Environment

def test_devnull_setter():
    env = Environment()
    assert env._devnull is None  # Initial state

    new_devnull = "new_devnull_value"
    env.devnull = new_devnull
    assert env._devnull == new_devnull  # Check if the setter works correctly
