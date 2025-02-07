# file: httpie/context.py:116-120
# asked: {"lines": [116, 117, 118, 119, 120], "branches": [[118, 119], [118, 120]]}
# gained: {"lines": [116, 117, 118, 119, 120], "branches": [[118, 119], [118, 120]]}

import pytest
import os
from httpie.context import Environment
from io import TextIOWrapper

def test_devnull_property():
    env = Environment(devnull=None)
    
    # Ensure _devnull is initially None
    assert env._devnull is None
    
    # Access the devnull property, which should trigger the lazy initialization
    devnull = env.devnull
    
    # Verify that _devnull is now set and is an open file object
    assert env._devnull is not None
    assert isinstance(env._devnull, TextIOWrapper)
    assert not env._devnull.closed
    
    # Clean up by closing the file
    env._devnull.close()
    assert env._devnull.closed

def test_devnull_property_already_set():
    with open(os.devnull, 'w+') as f:
        env = Environment(devnull=f)
        
        # Ensure _devnull is already set
        assert env._devnull is f
        
        # Access the devnull property, which should return the already set value
        devnull = env.devnull
        
        # Verify that _devnull is still the same file object
        assert env._devnull is f
        assert not env._devnull.closed

        # No need to clean up as the file was not opened by the property
