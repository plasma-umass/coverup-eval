# file sanic/response.py:499-524
# lines [499, 501, 502, 503, 514, 517, 520, 522, 523]
# branches []

import pytest
from sanic.response import HTTPResponse, redirect

def test_redirect():
    # Test with default parameters
    response = redirect("/test")
    assert response.status == 302
    assert response.headers["Location"] == "/test"
    assert response.content_type == "text/html; charset=utf-8"

    # Test with custom status
    response = redirect("/test", status=301)
    assert response.status == 301
    assert response.headers["Location"] == "/test"

    # Test with custom headers
    custom_headers = {"X-Custom-Header": "value"}
    response = redirect("/test", headers=custom_headers)
    assert response.status == 302
    assert response.headers["Location"] == "/test"
    assert response.headers["X-Custom-Header"] == "value"

    # Test with fully qualified URL
    response = redirect("http://example.com/test")
    assert response.status == 302
    assert response.headers["Location"] == "http://example.com/test"

    # Test with special characters in URL
    response = redirect("/test?param=value&other=äöü")
    assert response.status == 302
    assert response.headers["Location"] == "/test?param=value&other=%C3%A4%C3%B6%C3%BC"

    # Test with custom content type
    response = redirect("/test", content_type="application/json")
    assert response.status == 302
    assert response.headers["Location"] == "/test"
    assert response.content_type == "application/json"
