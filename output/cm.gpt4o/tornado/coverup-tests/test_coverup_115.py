# file tornado/httpclient.py:565-567
# lines [565, 566, 567]
# branches []

import pytest
from tornado.httpclient import HTTPRequest

def test_http_request_body_property():
    class TestHTTPRequest(HTTPRequest):
        def __init__(self, body):
            self._body = body

    # Create an instance of the TestHTTPRequest with a sample body
    request = TestHTTPRequest(b"sample body")

    # Assert that the body property returns the correct value
    assert request.body == b"sample body"
