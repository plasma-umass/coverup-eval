# file sanic/response.py:239-248
# lines [239, 240, 248]
# branches []

import pytest
from sanic.response import empty, HTTPResponse

def test_empty_response():
    # Test default parameters
    response = empty()
    assert isinstance(response, HTTPResponse)
    assert response.status == 204
    assert response.body == b""
    assert response.headers == {}

    # Test custom status
    response = empty(status=202)
    assert response.status == 202

    # Test custom headers
    custom_headers = {"X-Custom-Header": "value"}
    response = empty(headers=custom_headers)
    assert response.headers == custom_headers

    # Test custom status and headers
    response = empty(status=202, headers=custom_headers)
    assert response.status == 202
    assert response.headers == custom_headers
