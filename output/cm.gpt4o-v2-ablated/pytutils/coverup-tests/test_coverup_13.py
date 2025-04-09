# file: pytutils/lazy/lazy_regex.py:147-151
# asked: {"lines": [147, 149, 150, 151], "branches": []}
# gained: {"lines": [147, 149, 150, 151], "branches": []}

import pytest
import pickle

from pytutils.lazy.lazy_regex import LazyRegex

@pytest.fixture
def lazy_regex():
    return LazyRegex()

def test_lazy_regex_setstate(lazy_regex):
    state = {"args": ("pattern",), "kwargs": {"flags": 0}}
    lazy_regex.__setstate__(state)
    
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == ("pattern",)
    assert lazy_regex._regex_kwargs == {"flags": 0}
