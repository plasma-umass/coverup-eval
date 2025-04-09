# file sanic/headers.py:139-157
# lines [139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 154, 155, 156, 157]
# branches ['142->143', '142->157', '143->142', '143->144', '145->146', '145->147', '147->148', '147->149', '149->150', '149->151', '151->152', '151->154']

import pytest
from sanic.headers import fwd_normalize

def test_fwd_normalize():
    fwd = [
        ("by", "192.168.0.1"),
        ("for", "192.168.0.2"),
        ("host", "EXAMPLE.COM"),
        ("proto", "HTTP"),
        ("port", "8080"),
        ("path", "/some%20path"),
        ("unknown", "value"),
        ("port", "invalid_port"),  # This should trigger the ValueError and be skipped
    ]

    result = fwd_normalize(fwd)

    assert result["by"] == "192.168.0.1"  # Assuming fwd_normalize_address returns the same value
    assert result["for"] == "192.168.0.2"  # Assuming fwd_normalize_address returns the same value
    assert result["host"] == "example.com"
    assert result["proto"] == "http"
    assert result["port"] == 8080
    assert result["path"] == "/some path"
    assert result["unknown"] == "value"
    assert "invalid_port" not in result  # Ensure invalid port is skipped
