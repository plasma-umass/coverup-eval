# file: pytutils/lazy/lazy_regex.py:173-179
# asked: {"lines": [173, 179], "branches": []}
# gained: {"lines": [173, 179], "branches": []}

import pytest
import re
from pytutils.lazy.lazy_regex import install_lazy_compile, reset_compile, lazy_compile

def test_install_lazy_compile(monkeypatch):
    # Backup the original re.compile
    original_compile = re.compile

    # Mock lazy_compile to verify it gets assigned
    def mock_lazy_compile(*args, **kwargs):
        return "lazy_compile_called"
    
    monkeypatch.setattr('pytutils.lazy.lazy_regex.lazy_compile', mock_lazy_compile)

    # Call install_lazy_compile and check if re.compile is now lazy_compile
    install_lazy_compile()
    assert re.compile("test") == "lazy_compile_called"

    # Restore the original re.compile
    reset_compile()
    assert re.compile == original_compile
