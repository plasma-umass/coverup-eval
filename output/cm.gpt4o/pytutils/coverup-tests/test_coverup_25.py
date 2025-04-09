# file pytutils/lazy/lazy_regex.py:140-145
# lines [140, 142, 143, 144]
# branches []

import pytest
import pickle
from pytutils.lazy.lazy_regex import LazyRegex

class TestLazyRegex:
    def test___getstate__(self, mocker):
        # Create a subclass to avoid triggering the original LazyRegex behavior
        class TestableLazyRegex(LazyRegex):
            def __init__(self):
                self._regex_args = ('arg1', 'arg2')
                self._regex_kwargs = {'kwarg1': 'value1', 'kwarg2': 'value2'}
        
        # Create an instance of the subclass
        lazy_regex = TestableLazyRegex()
        
        # Get the state using __getstate__
        state = lazy_regex.__getstate__()
        
        # Assert the state is as expected
        assert state == {
            "args": ('arg1', 'arg2'),
            "kwargs": {'kwarg1': 'value1', 'kwarg2': 'value2'}
        }
