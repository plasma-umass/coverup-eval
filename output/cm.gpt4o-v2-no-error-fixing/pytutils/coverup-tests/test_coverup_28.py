# file: pytutils/lazy/lazy_regex.py:173-179
# asked: {"lines": [179], "branches": []}
# gained: {"lines": [179], "branches": []}

import pytest
import re
from pytutils.lazy.lazy_regex import install_lazy_compile, lazy_compile

def test_install_lazy_compile(monkeypatch):
    # Backup the original re.compile
    original_compile = re.compile

    # Ensure re.compile is not lazy_compile initially
    assert re.compile != lazy_compile

    # Install lazy_compile
    install_lazy_compile()

    # Check if re.compile is now lazy_compile
    assert re.compile == lazy_compile

    # Restore the original re.compile to avoid state pollution
    monkeypatch.setattr(re, 'compile', original_compile)

    # Ensure re.compile is restored to the original
    assert re.compile == original_compile
