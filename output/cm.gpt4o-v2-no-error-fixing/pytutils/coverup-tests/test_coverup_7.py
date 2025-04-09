# file: pytutils/lazy/lazy_regex.py:114-122
# asked: {"lines": [114, 120, 121, 122], "branches": []}
# gained: {"lines": [114, 120, 121, 122], "branches": []}

import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_lazy_regex_init():
    # Test with default arguments
    lazy_regex = LazyRegex()
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == ()
    assert lazy_regex._regex_kwargs == {}

    # Test with custom arguments
    args = ('pattern',)
    kwargs = {'flags': 0}
    lazy_regex = LazyRegex(args=args, kwargs=kwargs)
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == args
    assert lazy_regex._regex_kwargs == kwargs
