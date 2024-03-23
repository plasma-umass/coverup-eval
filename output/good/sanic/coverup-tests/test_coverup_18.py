# file sanic/headers.py:171-179
# lines [171, 175, 176, 177, 178, 179]
# branches ['176->177', '176->178']

import pytest
from sanic.headers import parse_host

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup if necessary after each test
    yield
    # Here you can put any cleanup logic if needed

def test_parse_host_with_port(cleanup):
    host_with_port = "example.com:8080"
    expected_result = ("example.com", 8080)
    assert parse_host(host_with_port) == expected_result

def test_parse_host_without_port(cleanup):
    host_without_port = "example.com"
    expected_result = ("example.com", None)
    assert parse_host(host_without_port) == expected_result

def test_parse_host_invalid(cleanup):
    invalid_host = "not a valid host"
    expected_result = (None, None)
    assert parse_host(invalid_host) == expected_result
