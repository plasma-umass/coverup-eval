# file tornado/escape.py:86-88
# lines [86, 88]
# branches []

import pytest
import re
from tornado.escape import squeeze

def test_squeeze():
    # Test with multiple spaces
    assert squeeze("a    b") == "a b"
    
    # Test with tabs and newlines
    assert squeeze("a\t\tb\n\nc") == "a b c"
    
    # Test with mixed whitespace characters
    assert squeeze("a \t\n b \x00 c") == "a b c"
    
    # Test with leading and trailing whitespace
    assert squeeze("   a b c   ") == "a b c"
    
    # Test with no whitespace
    assert squeeze("abc") == "abc"
    
    # Test with only whitespace
    assert squeeze(" \t\n\x00 ") == ""
