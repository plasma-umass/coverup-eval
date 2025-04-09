# file: pytutils/lazy/lazy_regex.py:182-190
# asked: {"lines": [182, 190], "branches": []}
# gained: {"lines": [182, 190], "branches": []}

import re
import pytest
from pytutils.lazy.lazy_regex import reset_compile

def test_reset_compile(monkeypatch):
    # Save the original re.compile function
    original_compile = re.compile

    # Mock re.compile with a dummy function
    def mock_compile(pattern, flags=0):
        return pattern

    monkeypatch.setattr(re, 'compile', mock_compile)

    # Ensure re.compile is now the mock function
    assert re.compile('test') == 'test'

    # Call reset_compile to restore the original re.compile
    reset_compile()

    # Ensure re.compile is restored to the original function
    assert re.compile is original_compile

    # Ensure the original re.compile works as expected
    assert re.compile('test').pattern == 'test'
