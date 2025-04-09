# file: pytutils/lazy/lazy_regex.py:165-170
# asked: {"lines": [165, 170], "branches": []}
# gained: {"lines": [165, 170], "branches": []}

import pytest
from pytutils.lazy.lazy_regex import lazy_compile, LazyRegex

def test_lazy_compile():
    # Test that lazy_compile returns a LazyRegex object
    pattern = r'\d+'
    flags = 0
    lazy_regex = lazy_compile(pattern, flags)
    
    assert isinstance(lazy_regex, LazyRegex)
    assert lazy_regex._regex_args == (pattern, flags)
    assert lazy_regex._regex_kwargs == {}

    # Test with keyword arguments
    lazy_regex = lazy_compile(pattern, flags=flags)
    
    assert isinstance(lazy_regex, LazyRegex)
    assert lazy_regex._regex_args == (pattern,)
    assert lazy_regex._regex_kwargs == {'flags': flags}
