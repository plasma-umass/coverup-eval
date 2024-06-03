# file sanic/response.py:301-320
# lines [315, 316, 317, 318, 319]
# branches []

import pytest
from sanic.response import raw, HTTPResponse

def test_raw_response():
    body = b"Test body"
    status = 201
    headers = {"X-Custom-Header": "value"}
    content_type = "application/test"

    response = raw(body=body, status=status, headers=headers, content_type=content_type)

    assert isinstance(response, HTTPResponse)
    assert response.body == body
    assert response.status == status
    assert response.headers.get("X-Custom-Header") == "value"
    assert response.content_type == content_type
