# file: pytutils/lazy/lazy_regex.py:182-190
# asked: {"lines": [182, 190], "branches": []}
# gained: {"lines": [182, 190], "branches": []}

import re
import pytest
from pytutils.lazy.lazy_regex import reset_compile

def test_reset_compile(monkeypatch):
    # Backup the original re.compile
    original_compile = re.compile

    # Mock re.compile to a dummy function
    def dummy_compile(pattern, flags=0):
        return pattern

    monkeypatch.setattr(re, 'compile', dummy_compile)

    # Ensure re.compile is now the dummy function
    assert re.compile('test') == 'test'

    # Call reset_compile to restore the original re.compile
    reset_compile()

    # Ensure re.compile is restored to the original function
    assert re.compile is original_compile

    # Clean up by resetting re.compile to its original state
    re.compile = original_compile
