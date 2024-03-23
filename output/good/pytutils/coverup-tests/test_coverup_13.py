# file pytutils/lazy/lazy_regex.py:140-145
# lines [140, 142, 143, 144]
# branches []

import pytest
from pytutils.lazy.lazy_regex import LazyRegex

class TestLazyRegex:
    def test_lazy_regex_getstate(self, mocker):
        # Create a mock for the LazyRegex object
        lazy_regex = mocker.Mock(spec=LazyRegex)
        lazy_regex._regex_args = ('pattern',)
        lazy_regex._regex_kwargs = {'flags': 0}

        # Call __getstate__ to simulate pickling
        state = LazyRegex.__getstate__(lazy_regex)

        # Assert that the state contains the correct items
        assert state == {
            "args": ('pattern',),
            "kwargs": {'flags': 0},
        }
