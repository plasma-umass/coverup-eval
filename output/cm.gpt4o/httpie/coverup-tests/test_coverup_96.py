# file httpie/context.py:116-120
# lines [118, 119, 120]
# branches ['118->119', '118->120']

import pytest
import os
from unittest.mock import patch
from httpie.context import Environment

@pytest.fixture
def environment():
    env = Environment()
    yield env
    if hasattr(env, '_devnull') and env._devnull is not None:
        env._devnull.close()
        env._devnull = None

def test_devnull_property(environment):
    # Ensure _devnull attribute is initialized to None
    environment._devnull = None

    devnull = environment.devnull
    assert devnull is not None
    assert devnull.name == os.devnull
    assert not devnull.closed

    # Ensure that the second access does not reopen the file
    with patch('builtins.open', side_effect=Exception('Should not be called')):
        devnull_again = environment.devnull
        assert devnull_again is devnull
