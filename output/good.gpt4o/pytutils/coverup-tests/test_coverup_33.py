# file pytutils/lazy/lazy_regex.py:173-179
# lines [173, 179]
# branches []

import pytest
import re
from pytutils.lazy.lazy_regex import install_lazy_compile

def lazy_compile(pattern, flags=0):
    """A mock lazy_compile function for testing purposes."""
    return re.compile(pattern, flags)

def test_install_lazy_compile(mocker):
    # Mock the lazy_compile function
    mock_lazy_compile = mocker.patch('pytutils.lazy.lazy_regex.lazy_compile', side_effect=lazy_compile)
    
    # Save the original re.compile function
    original_compile = re.compile
    
    # Call the function to test
    install_lazy_compile()
    
    # Assert that re.compile has been replaced by the mock lazy_compile
    assert re.compile == mock_lazy_compile
    
    # Clean up: restore the original re.compile function
    re.compile = original_compile
    
    # Assert that re.compile has been restored to its original function
    assert re.compile == original_compile
