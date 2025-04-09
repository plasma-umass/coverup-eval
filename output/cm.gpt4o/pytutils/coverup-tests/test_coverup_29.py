# file pytutils/lazy/lazy_import.py:194-203
# lines [194, 203]
# branches []

import pytest
from pytutils.lazy.lazy_import import disallow_proxying, ScopeReplacer

def test_disallow_proxying():
    # Ensure the initial state is True
    initial_state = ScopeReplacer._should_proxy
    assert initial_state is True

    # Call the function to disallow proxying
    disallow_proxying()

    # Verify that the state has changed to False
    assert ScopeReplacer._should_proxy is False

    # Clean up by resetting the state to its initial value
    ScopeReplacer._should_proxy = initial_state
