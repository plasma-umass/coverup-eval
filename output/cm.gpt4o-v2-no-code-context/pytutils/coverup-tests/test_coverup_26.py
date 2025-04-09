# file: pytutils/lazy/lazy_regex.py:173-179
# asked: {"lines": [173, 179], "branches": []}
# gained: {"lines": [173, 179], "branches": []}

import pytest
import re
from pytutils.lazy.lazy_regex import install_lazy_compile, reset_compile, lazy_compile

def test_install_lazy_compile(monkeypatch):
    # Backup the original re.compile
    original_compile = re.compile

    # Ensure re.compile is not lazy_compile initially
    assert re.compile is not lazy_compile

    # Install lazy_compile
    install_lazy_compile()

    # Verify that re.compile is now lazy_compile
    assert re.compile is lazy_compile

    # Restore the original re.compile
    reset_compile()

    # Verify that re.compile is restored to the original
    assert re.compile is original_compile

    # Clean up by ensuring re.compile is back to the original
    monkeypatch.setattr(re, 'compile', original_compile)
