# file: pytutils/lazy/lazy_regex.py:147-151
# asked: {"lines": [147, 149, 150, 151], "branches": []}
# gained: {"lines": [147, 149, 150, 151], "branches": []}

import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_lazy_regex_setstate():
    # Create a LazyRegex instance
    regex = LazyRegex(args=("pattern",), kwargs={"flags": 0})
    
    # Create a state dictionary to simulate the pickled state
    state = {"args": ("new_pattern",), "kwargs": {"flags": 1}}
    
    # Call __setstate__ to restore the state
    regex.__setstate__(state)
    
    # Assert that the state has been restored correctly
    assert regex._real_regex is None
    assert regex._regex_args == ("new_pattern",)
    assert regex._regex_kwargs == {"flags": 1}
