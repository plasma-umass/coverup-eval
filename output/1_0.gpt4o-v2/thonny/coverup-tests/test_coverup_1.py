# file: thonny/token_utils.py:5-7
# asked: {"lines": [5, 7], "branches": []}
# gained: {"lines": [5, 7], "branches": []}

import pytest
from thonny.token_utils import matches_any

def test_matches_any():
    # Test with a simple case
    result = matches_any("test", ["a", "b", "c"])
    assert result == "(?P<test>a|b|c)"
    
    # Test with an empty alternates list
    result = matches_any("empty", [])
    assert result == "(?P<empty>)"
    
    # Test with special characters in name and alternates
    result = matches_any("special", ["a$", "b^", "c*"])
    assert result == "(?P<special>a$|b^|c*)"
    
    # Test with numeric alternates
    result = matches_any("numbers", ["1", "2", "3"])
    assert result == "(?P<numbers>1|2|3)"
