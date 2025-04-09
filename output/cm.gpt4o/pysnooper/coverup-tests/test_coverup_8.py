# file pysnooper/utils.py:44-47
# lines [44, 45, 46]
# branches []

import pytest
from pysnooper.utils import shitcode

def test_shitcode():
    # Test with a string containing characters with ord values within the range 0 < ord(c) < 256
    assert shitcode("hello") == "hello"
    
    # Test with a string containing characters with ord values outside the range 0 < ord(c) < 256
    assert shitcode("hello\u0100world") == "hello?world"
    
    # Test with a string containing characters with ord values equal to 0
    assert shitcode("hello\0world") == "hello?world"
    
    # Test with a string containing characters with ord values equal to 256
    assert shitcode("hello\u0100world") == "hello?world"
    
    # Test with an empty string
    assert shitcode("") == ""
