# file: tornado/httpclient.py:565-567
# asked: {"lines": [565, 566, 567], "branches": []}
# gained: {"lines": [565, 566, 567], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest

def test_http_request_body_property():
    # Create an instance of HTTPRequest with a body
    request = HTTPRequest(url="http://example.com", body=b"test body")
    
    # Access the body property to ensure the getter is called
    assert request.body == b"test body"

    # Modify the body to ensure the setter is called
    request.body = b"new body"
    assert request.body == b"new body"

    # Clean up
    del request

