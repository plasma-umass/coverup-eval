# file: tornado/httpclient.py:565-567
# asked: {"lines": [565, 566, 567], "branches": []}
# gained: {"lines": [565, 566, 567], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest

def test_http_request_body_property():
    # Create an instance of HTTPRequest with a body
    request = HTTPRequest(url="http://example.com", body=b"test body")
    
    # Verify that the body property returns the correct value
    assert request.body == b"test body"

    # Modify the body and verify the change
    request.body = b"new body"
    assert request.body == b"new body"

    # Clean up
    del request

def test_http_request_body_property_with_string():
    # Create an instance of HTTPRequest with a string body
    request = HTTPRequest(url="http://example.com", body="test body")
    
    # Verify that the body property returns the correct value
    assert request.body == b"test body"

    # Modify the body and verify the change
    request.body = "new body"
    assert request.body == b"new body"

    # Clean up
    del request
