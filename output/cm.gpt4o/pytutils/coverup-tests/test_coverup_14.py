# file pytutils/lazy/lazy_regex.py:147-151
# lines [147, 149, 150, 151]
# branches []

import pytest
import pickle
from pytutils.lazy.lazy_regex import LazyRegex

def test_lazy_regex_setstate():
    # Create a LazyRegex instance
    lazy_regex = LazyRegex()
    
    # Create a dictionary to simulate the pickled state
    state = {
        "args": ("pattern",),
        "kwargs": {"flags": 0}
    }
    
    # Pickle and unpickle the LazyRegex instance to trigger __setstate__
    pickled_lazy_regex = pickle.dumps(lazy_regex)
    unpickled_lazy_regex = pickle.loads(pickled_lazy_regex)
    
    # Manually set the state to simulate unpickling
    unpickled_lazy_regex.__setstate__(state)
    
    # Assertions to verify the state has been restored correctly
    assert unpickled_lazy_regex._real_regex is None
    assert unpickled_lazy_regex._regex_args == ("pattern",)
    assert unpickled_lazy_regex._regex_kwargs == {"flags": 0}
