# file sanic/response.py:323-346
# lines [323, 325, 326, 335, 336, 337, 338, 339, 341, 342, 343, 344, 345]
# branches ['335->336', '335->341', '336->337', '336->338', '338->339', '338->341']

import pytest
from sanic.response import html, HTTPResponse

class HTMLable:
    def __html__(self):
        return "<p>HTMLable __html__</p>"

class HTMLRepr:
    def _repr_html_(self):
        return "<p>HTMLRepr _repr_html_</p>"

@pytest.fixture
def htmlable():
    return HTMLable()

@pytest.fixture
def htmlrepr():
    return HTMLRepr()

def test_html_with_str():
    response = html("<p>Test</p>")
    assert response.body == b"<p>Test</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_bytes():
    response = html(b"<p>Test</p>")
    assert response.body == b"<p>Test</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_htmlable(htmlable):
    response = html(htmlable)
    assert response.body == b"<p>HTMLable __html__</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_htmlrepr(htmlrepr):
    response = html(htmlrepr)
    assert response.body == b"<p>HTMLRepr _repr_html_</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_custom_status():
    response = html("<p>Test</p>", status=404)
    assert response.body == b"<p>Test</p>"
    assert response.status == 404
    assert response.content_type == "text/html; charset=utf-8"

def test_html_with_custom_headers():
    response = html("<p>Test</p>", headers={"X-Custom": "Value"})
    assert response.body == b"<p>Test</p>"
    assert response.status == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert response.headers["X-Custom"] == "Value"
