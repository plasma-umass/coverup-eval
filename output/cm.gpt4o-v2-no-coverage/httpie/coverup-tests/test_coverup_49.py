# file: httpie/context.py:122-124
# asked: {"lines": [122, 123, 124], "branches": []}
# gained: {"lines": [122, 123, 124], "branches": []}

import os
import pytest
from httpie.context import Environment

@pytest.fixture
def environment():
    env = Environment()
    yield env
    if env._devnull is not None:
        env._devnull.close()

def test_devnull_getter(environment):
    devnull = environment.devnull
    assert devnull is not None
    assert not devnull.closed

def test_devnull_setter(environment):
    with open(os.devnull, 'w+') as f:
        environment.devnull = f
        assert environment._devnull == f
