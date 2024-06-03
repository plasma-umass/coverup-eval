# file sanic/response.py:499-524
# lines [499, 501, 502, 503, 514, 517, 520, 522, 523]
# branches []

import pytest
from sanic.response import redirect, HTTPResponse
from urllib.parse import quote_plus

def test_redirect():
    # Test with default parameters
    response = redirect("/test")
    assert isinstance(response, HTTPResponse)
    assert response.status == 302
    assert response.headers["Location"] == quote_plus("/test", safe=":/%#?&=@[]!$&'()*+,;")
    assert response.content_type == "text/html; charset=utf-8"

    # Test with custom status code
    response = redirect("/test", status=301)
    assert response.status == 301

    # Test with custom headers
    custom_headers = {"X-Custom-Header": "value"}
    response = redirect("/test", headers=custom_headers)
    assert response.headers["X-Custom-Header"] == "value"
    assert response.headers["Location"] == quote_plus("/test", safe=":/%#?&=@[]!$&'()*+,;")

    # Test with fully qualified URL
    response = redirect("http://example.com/test")
    assert response.headers["Location"] == quote_plus("http://example.com/test", safe=":/%#?&=@[]!$&'()*+,;")

    # Test with custom content type
    response = redirect("/test", content_type="application/json")
    assert response.content_type == "application/json"
