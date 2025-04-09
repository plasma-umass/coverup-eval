# file pytutils/lazy/lazy_regex.py:173-179
# lines [173, 179]
# branches []

import re
import pytest
from pytutils.lazy.lazy_regex import install_lazy_compile, reset_compile, lazy_compile

def test_install_lazy_compile_restores_original_functionality(mocker):
    # Save the original re.compile function
    original_compile = re.compile
    
    # Mock the re.compile to simulate the original function
    mocker.patch('re.compile', side_effect=re.compile)
    
    # Install the lazy_compile as the default compile mode
    install_lazy_compile()
    
    # Check if re.compile is now pointing to lazy_compile
    assert re.compile == lazy_compile
    
    # Reset to original compile function
    reset_compile()
    
    # Check if re.compile has been restored to the original function
    assert re.compile == original_compile
