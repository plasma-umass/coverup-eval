# file: pytutils/lazy/lazy_regex.py:182-190
# asked: {"lines": [190], "branches": []}
# gained: {"lines": [190], "branches": []}

import pytest
import re
from pytutils.lazy.lazy_regex import reset_compile

def test_reset_compile(monkeypatch):
    # Backup the original re.compile
    original_compile = re.compile

    # Mock _real_re_compile to a dummy function
    def dummy_compile(pattern, flags=0):
        return pattern

    monkeypatch.setattr('pytutils.lazy.lazy_regex._real_re_compile', dummy_compile)

    # Ensure re.compile is not the dummy function initially
    assert re.compile != dummy_compile

    # Call reset_compile and check if re.compile is set to dummy_compile
    reset_compile()
    assert re.compile == dummy_compile

    # Call reset_compile again to ensure idempotency
    reset_compile()
    assert re.compile == dummy_compile

    # Restore the original re.compile
    re.compile = original_compile
    assert re.compile == original_compile
