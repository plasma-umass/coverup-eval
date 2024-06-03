# file httpie/context.py:99-100
# lines [99, 100]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Environment class is imported from httpie.context
from httpie.context import Environment

def test_environment_repr():
    env = Environment()
    repr_str = repr(env)
    assert repr_str == f'<Environment {env}>'
