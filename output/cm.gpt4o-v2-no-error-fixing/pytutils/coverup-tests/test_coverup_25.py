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

    # Clean up
    del lazy_regex

def test_lazy_compile_with_kwargs():
    # Test that lazy_compile returns a LazyRegex object with kwargs
    pattern = r'\d+'
    flags = 0
    lazy_regex = lazy_compile(pattern, flags, some_kwarg='value')
    
    assert isinstance(lazy_regex, LazyRegex)
    assert lazy_regex._regex_args == (pattern, flags)
    assert lazy_regex._regex_kwargs == {'some_kwarg': 'value'}

    # Clean up
    del lazy_regex
