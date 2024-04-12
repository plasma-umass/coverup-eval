# file pytutils/lazy/lazy_regex.py:182-190
# lines [182, 190]
# branches []

import re
from unittest.mock import patch
import pytest

# Assuming the module pytutils.lazy.lazy_regex has an attribute _real_re_compile
# which holds the reference to the original re.compile function.
from pytutils.lazy.lazy_regex import reset_compile, _real_re_compile

def test_reset_compile_restores_original_function(mocker):
    # Mock the re.compile function before calling reset_compile
    mocker.patch('re.compile', autospec=True)
    
    # Call the function that should restore the original re.compile
    reset_compile()
    
    # Assert that re.compile is the original compile function
    assert re.compile is _real_re_compile

    # No need to clean up with mocker.stopall() since mocker.patch automatically
    # does cleanup after the test function has finished executing.
