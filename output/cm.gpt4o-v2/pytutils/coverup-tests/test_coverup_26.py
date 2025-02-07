# file: pytutils/lazy/lazy_import.py:194-203
# asked: {"lines": [194, 203], "branches": []}
# gained: {"lines": [194, 203], "branches": []}

import pytest
from pytutils.lazy.lazy_import import disallow_proxying, ScopeReplacer

def test_disallow_proxying():
    # Ensure the initial state is True
    assert ScopeReplacer._should_proxy is True
    
    # Call the function to disallow proxying
    disallow_proxying()
    
    # Verify that the proxying is now disallowed
    assert ScopeReplacer._should_proxy is False
    
    # Clean up by resetting the state to True
    ScopeReplacer._should_proxy = True
