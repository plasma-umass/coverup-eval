# file: pytutils/lazy/lazy_regex.py:140-145
# asked: {"lines": [140, 142, 143, 144], "branches": []}
# gained: {"lines": [140, 142, 143, 144], "branches": []}

import pytest
import pickle
from pytutils.lazy.lazy_regex import LazyRegex

def test_lazy_regex_getstate():
    # Create an instance of LazyRegex
    regex = LazyRegex(args=("pattern",), kwargs={"flags": 0})
    
    # Get the state using __getstate__
    state = regex.__getstate__()
    
    # Assert that the state contains the correct args and kwargs
    assert state["args"] == ("pattern",)
    assert state["kwargs"] == {"flags": 0}

def test_lazy_regex_pickle():
    # Create an instance of LazyRegex
    regex = LazyRegex(args=("pattern",), kwargs={"flags": 0})
    
    # Pickle the instance
    pickled_regex = pickle.dumps(regex)
    
    # Unpickle the instance
    unpickled_regex = pickle.loads(pickled_regex)
    
    # Assert that the unpickled instance has the same state
    assert unpickled_regex._regex_args == ("pattern",)
    assert unpickled_regex._regex_kwargs == {"flags": 0}
