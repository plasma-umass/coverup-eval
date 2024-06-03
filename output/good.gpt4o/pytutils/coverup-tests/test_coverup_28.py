# file pytutils/lazy/lazy_regex.py:182-190
# lines [182, 190]
# branches []

import re
import pytest
from pytutils.lazy.lazy_regex import reset_compile

def test_reset_compile(mocker):
    # Mock the original re.compile function
    original_compile = re.compile
    mock_compile = mocker.patch('re.compile', return_value='mocked')

    # Ensure that re.compile is mocked
    assert re.compile('pattern') == 'mocked'

    # Call reset_compile to restore the original re.compile function
    reset_compile()

    # Ensure that re.compile is restored to the original function
    assert re.compile is original_compile

    # Clean up by resetting any changes made to re.compile
    reset_compile()
