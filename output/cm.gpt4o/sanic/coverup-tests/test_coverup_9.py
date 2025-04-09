# file sanic/headers.py:139-157
# lines [139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 154, 155, 156, 157]
# branches ['142->143', '142->157', '143->142', '143->144', '145->146', '145->147', '147->148', '147->149', '149->150', '149->151', '151->152', '151->154']

import pytest
from sanic.headers import fwd_normalize

def test_fwd_normalize():
    # Test data
    fwd = [
        ("by", "192.168.0.1"),
        ("for", "192.168.0.2"),
        ("host", "EXAMPLE.COM"),
        ("proto", "HTTP"),
        ("port", "8080"),
        ("path", "/some%20path"),
        ("unknown", "value"),
        ("port", "invalid_port"),  # This should trigger ValueError and be ignored
    ]

    # Expected result
    expected = {
        "by": "192.168.0.1",
        "for": "192.168.0.2",
        "host": "example.com",
        "proto": "http",
        "port": 8080,
        "path": "/some path",
        "unknown": "value"
    }

    # Call the function
    result = fwd_normalize(fwd)

    # Assertions
    assert result == expected

