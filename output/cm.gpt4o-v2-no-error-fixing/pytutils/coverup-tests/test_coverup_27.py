# file: pytutils/lazy/lazy_regex.py:182-190
# asked: {"lines": [182, 190], "branches": []}
# gained: {"lines": [182, 190], "branches": []}

import pytest
import re
from pytutils.lazy.lazy_regex import reset_compile, lazy_compile

def test_reset_compile(monkeypatch):
    # Backup the original re.compile
    original_compile = re.compile

    # Mock _real_re_compile to a dummy function
    def mock_real_compile(pattern, flags=0):
        return "mocked"
    
    monkeypatch.setattr('pytutils.lazy.lazy_regex._real_re_compile', mock_real_compile)
    
    # Override re.compile with lazy_compile
    re.compile = lazy_compile
    
    # Ensure re.compile is overridden
    assert re.compile == lazy_compile
    
    # Call reset_compile to restore the original re.compile
    reset_compile()
    
    # Check if re.compile is restored to the original or mocked function
    assert re.compile == mock_real_compile
    
    # Clean up: Restore the original re.compile
    re.compile = original_compile
