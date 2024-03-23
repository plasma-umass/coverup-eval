# file thonny/token_utils.py:5-7
# lines [5, 7]
# branches []

import pytest
from thonny.token_utils import matches_any

def test_matches_any():
    # Test with a single alternate
    single_alternate = matches_any("test_single", ["single"])
    assert single_alternate == "(?P<test_single>single)"
    
    # Test with multiple alternates
    multiple_alternates = matches_any("test_multiple", ["multi", "ple"])
    assert multiple_alternates == "(?P<test_multiple>multi|ple)"
    
    # Test with no alternates
    no_alternates = matches_any("test_none", [])
    assert no_alternates == "(?P<test_none>)"
    
    # Test with special regex characters to ensure they are not treated as regex operators
    special_chars_alternates = matches_any("test_special", ["a|b", "(c)", "[d-e]"])
    assert special_chars_alternates == "(?P<test_special>a|b|(c)|[d-e])"
