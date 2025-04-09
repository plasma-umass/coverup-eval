# file pytutils/lazy/lazy_regex.py:147-151
# lines [147, 149, 150, 151]
# branches []

import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_lazy_regex_setstate():
    # Create a LazyRegex instance and simulate the pickled state
    lazy_regex = LazyRegex()
    pickled_state = {
        'args': ('pattern',),
        'kwargs': {'flags': 0}
    }

    # Use the __setstate__ method to restore the state
    lazy_regex.__setstate__(pickled_state)

    # Check if the state has been restored correctly
    assert lazy_regex._regex_args == ('pattern',)
    assert lazy_regex._regex_kwargs == {'flags': 0}

    # Check if _real_regex is set to None
    assert lazy_regex._real_regex is None
