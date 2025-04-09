# file: pytutils/lazy/lazy_regex.py:173-179
# asked: {"lines": [179], "branches": []}
# gained: {"lines": [179], "branches": []}

import re
import pytest
from pytutils.lazy.lazy_regex import install_lazy_compile

def lazy_compile(pattern, flags=0):
    """A mock lazy_compile function for testing purposes."""
    return re._compile(pattern, flags)

def test_install_lazy_compile(monkeypatch):
    # Backup the original re.compile
    original_compile = re.compile

    # Mock lazy_compile function
    monkeypatch.setattr('pytutils.lazy.lazy_regex.lazy_compile', lazy_compile)

    # Call the function to install lazy_compile
    install_lazy_compile()

    # Assert that re.compile is now lazy_compile
    assert re.compile == lazy_compile

    # Restore the original re.compile
    re.compile = original_compile

    # Assert that re.compile is restored to the original
    assert re.compile == original_compile
