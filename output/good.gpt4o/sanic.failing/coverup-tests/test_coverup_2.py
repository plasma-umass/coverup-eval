# file sanic/headers.py:160-168
# lines [160, 162, 163, 164, 165, 166, 167, 168]
# branches ['162->163', '162->164', '164->165', '164->166', '166->167', '166->168']

import pytest
from sanic.headers import fwd_normalize_address

def test_fwd_normalize_address():
    # Test for ValueError when addr is "unknown"
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")
    
    # Test for obfuscated strings starting with "_"
    assert fwd_normalize_address("_obfuscated") == "_obfuscated"
    
    # Test for IPv6 address normalization
    assert fwd_normalize_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == "[2001:0db8:85a3:0000:0000:8a2e:0370:7334]"
    
    # Test for lower-casing of normal addresses
    assert fwd_normalize_address("NORMAL") == "normal"
