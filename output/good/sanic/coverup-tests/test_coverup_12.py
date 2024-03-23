# file sanic/headers.py:160-168
# lines [160, 162, 163, 164, 165, 166, 167, 168]
# branches ['162->163', '162->164', '164->165', '164->166', '166->167', '166->168']

import pytest
from sanic.headers import fwd_normalize_address
import re

_ipv6_re = re.compile(
    r"([0-9a-fA-F:]+:+)+[0-9a-fA-F]{1,4}|::|[0-9a-fA-F]{1,4}"
)

def test_fwd_normalize_address_unknown():
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")

def test_fwd_normalize_address_obfuscated():
    assert fwd_normalize_address("_obfuscated") == "_obfuscated"

def test_fwd_normalize_address_ipv6():
    assert fwd_normalize_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == "[2001:0db8:85a3:0000:0000:8a2e:0370:7334]"

def test_fwd_normalize_address_lowercase():
    assert fwd_normalize_address("EXAMPLE.COM") == "example.com"
