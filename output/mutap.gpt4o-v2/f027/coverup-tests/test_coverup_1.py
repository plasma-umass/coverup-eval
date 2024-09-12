# file: f027/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f027 import flip_case

def test_flip_case():
    # Test with a mixed case string
    assert flip_case("Hello World") == "hELLO wORLD"
    
    # Test with an all lowercase string
    assert flip_case("hello") == "HELLO"
    
    # Test with an all uppercase string
    assert flip_case("WORLD") == "world"
    
    # Test with a string with numbers and special characters
    assert flip_case("1234!@#$") == "1234!@#$"
    
    # Test with an empty string
    assert flip_case("") == ""
