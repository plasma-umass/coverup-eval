# file: httpie/context.py:116-120
# asked: {"lines": [116, 117, 118, 119, 120], "branches": [[118, 119], [118, 120]]}
# gained: {"lines": [116, 117, 118, 119, 120], "branches": [[118, 119], [118, 120]]}

import os
import pytest
from httpie.context import Environment

@pytest.fixture
def env():
    return Environment()

def test_devnull_initialization(env):
    # Ensure _devnull is initially None
    assert env._devnull is None

    # Access the devnull property to trigger initialization
    devnull = env.devnull

    # Verify that _devnull is now set and the file is opened
    assert env._devnull is not None
    assert not env._devnull.closed

    # Clean up by closing the file
    env._devnull.close()

def test_devnull_reuse(env):
    # Access the devnull property to trigger initialization
    devnull1 = env.devnull

    # Access the devnull property again to ensure the same file is reused
    devnull2 = env.devnull

    # Verify that the same file object is returned
    assert devnull1 is devnull2

    # Clean up by closing the file
    env._devnull.close()

def test_devnull_setter(env):
    # Create a mock file object
    mock_devnull = open(os.devnull, 'w+')

    # Set the devnull property to the mock file object
    env.devnull = mock_devnull

    # Verify that the _devnull attribute is set to the mock file object
    assert env._devnull is mock_devnull

    # Clean up by closing the file
    env._devnull.close()
