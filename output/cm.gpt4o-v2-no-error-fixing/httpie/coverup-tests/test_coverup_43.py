# file: httpie/context.py:99-100
# asked: {"lines": [99, 100], "branches": []}
# gained: {"lines": [99, 100], "branches": []}

import pytest
from httpie.context import Environment

def test_environment_repr():
    env = Environment()
    repr_str = repr(env)
    assert repr_str.startswith('<Environment ')
    assert repr_str.endswith('>')
