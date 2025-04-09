# file: pytutils/lazy/lazy_regex.py:173-179
# asked: {"lines": [173, 179], "branches": []}
# gained: {"lines": [173, 179], "branches": []}

import pytest
import re
from pytutils.lazy.lazy_regex import install_lazy_compile, lazy_compile

class LazyRegex:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
        self._compiled = None

    def compile(self):
        if self._compiled is None:
            self._compiled = re._compile(*self.args, **self.kwargs)
        return self._compiled

def test_install_lazy_compile(monkeypatch):
    original_compile = re.compile

    # Ensure re.compile is replaced by lazy_compile
    install_lazy_compile()
    assert re.compile == lazy_compile

    # Clean up: restore the original re.compile
    monkeypatch.setattr(re, 'compile', original_compile)
    assert re.compile == original_compile
