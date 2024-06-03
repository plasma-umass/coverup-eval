# file pytutils/lazy/lazy_regex.py:114-122
# lines [114, 120, 121, 122]
# branches []

import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_lazy_regex_initialization():
    # Test initialization with default arguments
    lazy_regex_default = LazyRegex()
    assert lazy_regex_default._real_regex is None
    assert lazy_regex_default._regex_args == ()
    assert lazy_regex_default._regex_kwargs == {}

    # Test initialization with custom arguments
    args = ('pattern',)
    kwargs = {'flags': 0}
    lazy_regex_custom = LazyRegex(args=args, kwargs=kwargs)
    assert lazy_regex_custom._real_regex is None
    assert lazy_regex_custom._regex_args == args
    assert lazy_regex_custom._regex_kwargs == kwargs
