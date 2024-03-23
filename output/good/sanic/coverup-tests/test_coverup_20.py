# file sanic/response.py:277-298
# lines [277, 279, 280, 281, 291, 292, 293, 296, 297]
# branches ['291->292', '291->296']

import pytest
from sanic.response import HTTPResponse, text

def test_text_response_with_string_body():
    # Test with a simple string body
    response = text("Hello, World!")
    assert response.status == 200
    assert response.body == b"Hello, World!"
    assert response.content_type == "text/plain; charset=utf-8"

def test_text_response_with_custom_status_headers_and_content_type():
    # Test with custom status, headers, and content type
    custom_headers = {'X-Custom-Header': 'Value'}
    response = text("Custom Response", status=201, headers=custom_headers, content_type="text/custom")
    assert response.status == 201
    assert response.body == b"Custom Response"
    assert response.headers['X-Custom-Header'] == 'Value'
    assert response.content_type == "text/custom"

def test_text_response_with_non_string_body():
    # Test with non-string body to hit the TypeError branch
    with pytest.raises(TypeError) as exc_info:
        text(body=123)
    assert "Bad body type. Expected str, got int" in str(exc_info.value)
