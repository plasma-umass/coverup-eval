# file sanic/response.py:301-320
# lines [301, 303, 304, 305, 315, 316, 317, 318, 319]
# branches []

import pytest
from sanic.response import HTTPResponse, raw, DEFAULT_HTTP_CONTENT_TYPE

@pytest.mark.parametrize("body,status,headers,content_type", [
    (b'binary data', 200, None, DEFAULT_HTTP_CONTENT_TYPE),
    ('text data', 201, {'X-Custom-Header': 'value'}, 'text/plain'),
    (None, 204, {'X-Another-Header': 'another value'}, 'application/json'),
])
def test_raw_response(body, status, headers, content_type):
    response = raw(body, status, headers, content_type)

    assert response.status == status
    if body is not None:
        expected_body = body if isinstance(body, bytes) else body.encode('utf-8')
    else:
        expected_body = b''
    assert response.body == expected_body
    assert response.content_type == content_type
    if headers:
        for key, value in headers.items():
            assert response.headers[key] == value
