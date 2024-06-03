# file sanic/response.py:53-58
# lines [53, 54, 55, 56, 57]
# branches ['54->55', '54->56']

import pytest
from sanic.response import BaseHTTPResponse

@pytest.fixture
def response():
    return BaseHTTPResponse()

def test_encode_body_none(response):
    result = response._encode_body(None)
    assert result == b""

def test_encode_body_str(response):
    result = response._encode_body("test")
    assert result == b"test"

def test_encode_body_bytes(response):
    result = response._encode_body(b"test")
    assert result == b"test"
