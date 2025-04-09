# file: httpie/core.py:221-231
# asked: {"lines": [221, 222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}
# gained: {"lines": [221, 222, 223, 224, 225, 226, 227, 229, 230, 231], "branches": []}

import pytest
import platform
import sys
from io import StringIO
from httpie.context import Environment
from httpie.core import print_debug_info

def test_print_debug_info(monkeypatch):
    # Create a mock stderr
    mock_stderr = StringIO()
    
    # Create an environment with the mock stderr
    env = Environment(stderr=mock_stderr)
    
    # Call the function
    print_debug_info(env)
    
    # Get the output
    output = mock_stderr.getvalue()
    
    # Assertions to verify the output contains expected substrings
    assert 'HTTPie' in output
    assert 'Requests' in output
    assert 'Pygments' in output
    assert 'Python' in output
    assert platform.system() in output
    assert platform.release() in output
    assert repr(env) in output
    
    # Clean up
    mock_stderr.close()
