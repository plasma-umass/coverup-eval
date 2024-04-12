# file sanic/response.py:44-51
# lines [44, 45, 46, 47, 48, 49, 50, 51]
# branches []

import pytest
from sanic.response import BaseHTTPResponse
from sanic.http import Http
from sanic.cookies import CookieJar
from multidict import CIMultiDict

@pytest.fixture
def base_http_response():
    return BaseHTTPResponse()

def test_base_http_response_initialization(base_http_response):
    assert base_http_response.asgi is False
    assert base_http_response.body is None
    assert base_http_response.content_type is None
    assert base_http_response.stream is None
    assert base_http_response.status is None
    assert isinstance(base_http_response.headers, CIMultiDict)
    assert base_http_response._cookies is None or isinstance(base_http_response._cookies, CookieJar)
