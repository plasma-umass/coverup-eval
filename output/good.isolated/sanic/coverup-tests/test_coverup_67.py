# file sanic/response.py:207-236
# lines [207, 208, 221, 223, 225, 226, 227, 228, 230, 232, 233, 234, 235, 236]
# branches []

import pytest
from sanic.response import HTTPResponse
from sanic.http import Header

@pytest.fixture
def response():
    return HTTPResponse()

def test_httpresponse_init_default(response):
    assert response.status == 200
    assert response.body == b''
    assert response.content_type is None
    assert isinstance(response.headers, Header)
    assert response._cookies is None

def test_httpresponse_init_with_params():
    body = 'Hello, World!'
    status = 404
    headers = {'Content-Language': 'en'}
    content_type = 'text/plain'
    response = HTTPResponse(body=body, status=status, headers=headers, content_type=content_type)
    
    assert response.status == status
    assert response.body == body.encode()
    assert response.content_type == content_type
    assert response.headers['Content-Language'] == 'en'
    assert response._cookies is None
