# file: pytutils/lazy/lazy_import.py:194-203
# asked: {"lines": [194, 203], "branches": []}
# gained: {"lines": [194, 203], "branches": []}

import pytest
from pytutils.lazy.lazy_import import disallow_proxying, ScopeReplacer

@pytest.fixture(autouse=True)
def reset_scope_replacer():
    # Ensure that ScopeReplacer._should_proxy is reset after each test
    original_value = ScopeReplacer._should_proxy
    yield
    ScopeReplacer._should_proxy = original_value

def test_disallow_proxying():
    # Ensure that ScopeReplacer._should_proxy is initially True
    assert ScopeReplacer._should_proxy is True
    
    # Call the function to disallow proxying
    disallow_proxying()
    
    # Verify that ScopeReplacer._should_proxy is now False
    assert ScopeReplacer._should_proxy is False
