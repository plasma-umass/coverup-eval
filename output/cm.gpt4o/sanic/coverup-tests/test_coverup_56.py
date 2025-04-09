# file sanic/response.py:323-346
# lines [323, 325, 326, 335, 336, 337, 338, 339, 341, 342, 343, 344, 345]
# branches ['335->336', '335->341', '336->337', '336->338', '338->339', '338->341']

import pytest
from sanic.response import html, HTTPResponse

class HTMLLikeObject:
    def __html__(self):
        return "<p>HTML content</p>"

class ReprHTMLLikeObject:
    def _repr_html_(self):
        return "<p>Repr HTML content</p>"

def test_html_with_str_body():
    response = html("<p>Test</p>")
    assert isinstance(response, HTTPResponse)
    assert response.body == b"<p>Test</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_bytes_body():
    response = html(b"<p>Test</p>")
    assert isinstance(response, HTTPResponse)
    assert response.body == b"<p>Test</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_html_like_object():
    obj = HTMLLikeObject()
    response = html(obj)
    assert isinstance(response, HTTPResponse)
    assert response.body == b"<p>HTML content</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_repr_html_like_object():
    obj = ReprHTMLLikeObject()
    response = html(obj)
    assert isinstance(response, HTTPResponse)
    assert response.body == b"<p>Repr HTML content</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_custom_status_and_headers():
    headers = {"X-Custom-Header": "value"}
    response = html("<p>Test</p>", status=404, headers=headers)
    assert isinstance(response, HTTPResponse)
    assert response.body == b"<p>Test</p>"
    assert response.status == 404
    assert response.content_type == "text/html; charset=utf-8"
    assert response.headers.get("X-Custom-Header") == "value"
