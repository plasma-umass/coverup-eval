# file sanic/response.py:44-51
# lines [44, 45, 46, 47, 48, 49, 50, 51]
# branches []

import pytest
from sanic.response import BaseHTTPResponse
from sanic.http import Http
from sanic.cookies import CookieJar

def test_base_http_response_initialization():
    response = BaseHTTPResponse()
    
    assert response.asgi == False
    assert response.body is None
    assert response.content_type is None
    assert response.stream is None
    assert response.status is None
    assert response.headers is not None
    assert response._cookies is None
