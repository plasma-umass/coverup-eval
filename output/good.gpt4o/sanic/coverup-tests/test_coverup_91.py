# file sanic/headers.py:139-157
# lines []
# branches ['143->142']

import pytest
from sanic.headers import fwd_normalize

def test_fwd_normalize_with_none_value():
    fwd = [("by", "127.0.0.1"), ("for", None), ("host", "EXAMPLE.COM"), ("proto", "HTTP"), ("port", "8080"), ("path", "/test%20path")]
    result = fwd_normalize(fwd)
    
    assert result == {
        "by": "127.0.0.1",
        "host": "example.com",
        "proto": "http",
        "port": 8080,
        "path": "/test path"
    }
