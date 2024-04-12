# file pytutils/lazy/lazy_regex.py:165-170
# lines [165, 170]
# branches []

import pytest
from unittest.mock import patch
from pytutils.lazy.lazy_regex import lazy_compile

class TestLazyRegex:
    def test_lazy_compile(self, mocker):
        # Mock the LazyRegex class to ensure it is called correctly
        mock_lazy_regex = mocker.patch('pytutils.lazy.lazy_regex.LazyRegex')

        # Call the lazy_compile function with test arguments
        args = ('test_pattern',)
        kwargs = {'flags': 0}
        result = lazy_compile(*args, **kwargs)

        # Assert that the LazyRegex class was instantiated with the correct arguments
        mock_lazy_regex.assert_called_once_with(args, kwargs)

        # Assert that the result is an instance of the mock
        assert result == mock_lazy_regex.return_value

        # Clean up by unpatching the LazyRegex class
        mocker.stopall()
