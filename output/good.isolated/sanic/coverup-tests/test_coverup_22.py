# file sanic/response.py:53-58
# lines [53, 54, 55, 56, 57]
# branches ['54->55', '54->56']

import pytest
from sanic.response import BaseHTTPResponse

@pytest.fixture
def base_http_response():
    return BaseHTTPResponse()

def test_encode_body_with_none(base_http_response):
    assert base_http_response._encode_body(None) == b""

def test_encode_body_with_str(base_http_response):
    test_str = "test"
    assert base_http_response._encode_body(test_str) == test_str.encode()

def test_encode_body_with_bytes(base_http_response):
    test_bytes = b"test"
    assert base_http_response._encode_body(test_bytes) == test_bytes
