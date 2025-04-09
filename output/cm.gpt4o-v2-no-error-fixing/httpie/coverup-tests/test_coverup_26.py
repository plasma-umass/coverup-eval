# file: httpie/context.py:116-120
# asked: {"lines": [116, 117, 118, 119, 120], "branches": [[118, 119], [118, 120]]}
# gained: {"lines": [116, 117, 118, 119, 120], "branches": [[118, 119], [118, 120]]}

import pytest
import os
from httpie.context import Environment

def test_devnull_property():
    env = Environment(devnull=None)
    assert env._devnull is None  # Ensure initial state
    devnull = env.devnull
    assert devnull is not None  # Ensure devnull is set
    assert env._devnull is not None  # Ensure _devnull is set
    assert devnull == env._devnull  # Ensure devnull property returns _devnull

    # Clean up
    devnull.close()
    env._devnull = None

def test_devnull_property_already_set():
    with open(os.devnull, 'w+') as f:
        env = Environment(devnull=f)
        assert env._devnull is f  # Ensure initial state
        devnull = env.devnull
        assert devnull is f  # Ensure devnull property returns the already set _devnull

        # No need to clean up as the file was not created by the property
