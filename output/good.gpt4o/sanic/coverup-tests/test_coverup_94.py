# file sanic/headers.py:171-179
# lines [175, 176, 177, 178, 179]
# branches ['176->177', '176->178']

import pytest
from sanic.headers import parse_host

def test_parse_host_invalid_host():
    # Test with an invalid host string that does not match the regex
    host, port = parse_host("invalid_host")
    assert host is None
    assert port is None

def test_parse_host_valid_host_with_port():
    # Test with a valid host string with a port
    host, port = parse_host("example.com:8080")
    assert host == "example.com"
    assert port == 8080

def test_parse_host_valid_host_without_port():
    # Test with a valid host string without a port
    host, port = parse_host("example.com")
    assert host == "example.com"
    assert port is None
