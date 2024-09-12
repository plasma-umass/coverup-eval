# file: f051/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f051 import remove_vowels

def test_remove_vowels():
    # Test with a string containing vowels
    assert remove_vowels("hello") == "hll"
    
    # Test with a string containing no vowels
    assert remove_vowels("bcdfg") == "bcdfg"
    
    # Test with an empty string
    assert remove_vowels("") == ""
    
    # Test with a string containing uppercase vowels
    assert remove_vowels("HELLO") == "HLL"
    
    # Test with a string containing mixed case vowels
    assert remove_vowels("HeLLo") == "HLL"
    
    # Test with a string containing only vowels
    assert remove_vowels("aeiouAEIOU") == ""
