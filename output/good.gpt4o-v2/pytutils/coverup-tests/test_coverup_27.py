# file: pytutils/lazy/lazy_regex.py:182-190
# asked: {"lines": [182, 190], "branches": []}
# gained: {"lines": [182, 190], "branches": []}

import pytest
import re
from pytutils.lazy.lazy_regex import reset_compile

def test_reset_compile(monkeypatch):
    # Backup the original re.compile
    original_compile = re.compile

    # Mock _real_re_compile to a dummy function
    def dummy_compile(pattern, flags=0):
        return "dummy"

    monkeypatch.setattr('pytutils.lazy.lazy_regex._real_re_compile', dummy_compile)

    # Change re.compile to something else
    re.compile = lambda pattern, flags=0: "changed"

    # Ensure re.compile is changed
    assert re.compile("test") == "changed"

    # Call reset_compile and check if re.compile is restored to _real_re_compile
    reset_compile()
    assert re.compile("test") == "dummy"

    # Call reset_compile again to ensure idempotency
    reset_compile()
    assert re.compile("test") == "dummy"

    # Restore the original re.compile
    re.compile = original_compile
    assert re.compile("test").pattern == "test"
