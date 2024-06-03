# file pytutils/lazy/lazy_regex.py:165-170
# lines [165, 170]
# branches []

import pytest
from pytutils.lazy.lazy_regex import lazy_compile

class LazyRegex:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
        self._compiled = None

    def compile(self):
        if self._compiled is None:
            import re
            self._compiled = re.compile(*self.args, **self.kwargs)
        return self._compiled

def test_lazy_compile(mocker):
    # Mock the LazyRegex class to ensure it is being called correctly
    mock_lazy_regex = mocker.patch('pytutils.lazy.lazy_regex.LazyRegex', autospec=True)
    
    # Call the lazy_compile function with some arguments
    args = ('pattern',)
    kwargs = {'flags': 0}
    result = lazy_compile(*args, **kwargs)
    
    # Assert that LazyRegex was called with the correct arguments
    mock_lazy_regex.assert_called_once_with(args, kwargs)
    
    # Assert that the result is the mock instance of LazyRegex
    assert result == mock_lazy_regex.return_value
    
    # Clean up by resetting the mock
    mock_lazy_regex.reset_mock()
