# file httpie/context.py:99-100
# lines [99, 100]
# branches []

import pytest
from httpie.context import Environment

def test_environment_repr():
    env = Environment()
    repr_string = repr(env)
    assert repr_string.startswith('<Environment')
    assert repr_string.endswith('>')
