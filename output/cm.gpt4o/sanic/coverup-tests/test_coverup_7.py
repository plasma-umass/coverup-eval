# file sanic/response.py:277-298
# lines [277, 279, 280, 281, 291, 292, 293, 296, 297]
# branches ['291->292', '291->296']

import pytest
from sanic.response import text, HTTPResponse

def test_text_response():
    # Test with valid string body
    response = text("Hello, world!")
    assert isinstance(response, HTTPResponse)
    assert response.body == b"Hello, world!"
    assert response.status == 200
    assert response.content_type == "text/plain; charset=utf-8"

    # Test with custom status
    response = text("Hello, world!", status=404)
    assert response.status == 404

    # Test with custom headers
    custom_headers = {"X-Custom-Header": "value"}
    response = text("Hello, world!", headers=custom_headers)
    assert response.headers["X-Custom-Header"] == "value"

    # Test with custom content type
    response = text("Hello, world!", content_type="text/html")
    assert response.content_type == "text/html"

    # Test with non-string body to raise TypeError
    with pytest.raises(TypeError):
        text(12345)

