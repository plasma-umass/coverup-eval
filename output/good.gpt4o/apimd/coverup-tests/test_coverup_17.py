# file apimd/parser.py:51-53
# lines [51, 53]
# branches []

import pytest
from apimd.parser import parent

def test_parent():
    # Test with default level
    assert parent("a.b.c.d") == "a.b.c"
    
    # Test with level 1
    assert parent("a.b.c.d", level=1) == "a.b.c"
    
    # Test with level 2
    assert parent("a.b.c.d", level=2) == "a.b"
    
    # Test with level 3
    assert parent("a.b.c.d", level=3) == "a"
    
    # Test with level 4 (more than the number of dots in the string)
    assert parent("a.b.c.d", level=4) == "a"
    
    # Test with level 0 (should return the full string)
    assert parent("a.b.c.d", level=0) == "a.b.c.d"
    
    # Test with a string without dots
    assert parent("abcd", level=1) == "abcd"
    
    # Test with a string without dots and level more than 0
    assert parent("abcd", level=2) == "abcd"
