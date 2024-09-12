# file: pytutils/lazy/lazy_regex.py:140-145
# asked: {"lines": [140, 142, 143, 144], "branches": []}
# gained: {"lines": [140, 142, 143, 144], "branches": []}

import pytest
import pickle
from pytutils.lazy.lazy_regex import LazyRegex

def test_lazy_regex_getstate():
    # Create an instance of LazyRegex with specific args and kwargs
    args = (r'\d+',)
    kwargs = {'flags': 0}
    lazy_regex = LazyRegex(args=args, kwargs=kwargs)
    
    # Get the state using __getstate__
    state = lazy_regex.__getstate__()
    
    # Assert that the state contains the correct args and kwargs
    assert state == {'args': args, 'kwargs': kwargs}

def test_lazy_regex_pickle():
    # Create an instance of LazyRegex with specific args and kwargs
    args = (r'\d+',)
    kwargs = {'flags': 0}
    lazy_regex = LazyRegex(args=args, kwargs=kwargs)
    
    # Pickle and unpickle the LazyRegex instance
    pickled_data = pickle.dumps(lazy_regex)
    unpickled_lazy_regex = pickle.loads(pickled_data)
    
    # Assert that the unpickled instance has the same state as the original
    assert unpickled_lazy_regex._regex_args == args
    assert unpickled_lazy_regex._regex_kwargs == kwargs
