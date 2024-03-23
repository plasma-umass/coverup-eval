# file pytutils/lazy/lazy_regex.py:114-122
# lines [114, 120, 121, 122]
# branches []

import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

def test_lazy_regex_initialization(mocker):
    # Mock re.compile to ensure it's not called during initialization
    mock_compile = mocker.patch('re.compile')

    # Initialize LazyRegex with some arguments
    args = ('pattern',)
    kwargs = {'flags': re.IGNORECASE}
    lazy_regex = LazyRegex(args=args, kwargs=kwargs)

    # Assert that re.compile was not called during initialization
    mock_compile.assert_not_called()

    # Assert that the internal state is correctly set
    assert lazy_regex._regex_args == args
    assert lazy_regex._regex_kwargs == kwargs

    # Cleanup is not necessary as we are using mocker to patch
