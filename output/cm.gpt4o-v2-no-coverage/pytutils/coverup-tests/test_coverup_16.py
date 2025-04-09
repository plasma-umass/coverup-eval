# file: pytutils/lazy/lazy_regex.py:147-151
# asked: {"lines": [147, 149, 150, 151], "branches": []}
# gained: {"lines": [147, 149, 150, 151], "branches": []}

import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_lazy_regex_setstate():
    # Create an instance of LazyRegex
    lazy_regex = LazyRegex(args=("pattern",), kwargs={"flags": 0})
    
    # Define the state to set
    state = {"args": ("new_pattern",), "kwargs": {"flags": 1}}
    
    # Call __setstate__ to restore the state
    lazy_regex.__setstate__(state)
    
    # Assert that the state has been restored correctly
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == ("new_pattern",)
    assert lazy_regex._regex_kwargs == {"flags": 1}
