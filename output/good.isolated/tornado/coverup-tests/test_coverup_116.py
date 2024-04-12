# file tornado/httpclient.py:569-571
# lines [569, 570, 571]
# branches []

import pytest
from tornado.httpclient import HTTPRequest
from tornado.escape import utf8

def test_http_request_body_setter():
    request = HTTPRequest(url='http://example.com')

    # Set the body using a string and verify it's correctly encoded to bytes
    test_string = "test body"
    request.body = test_string
    assert request._body == utf8(test_string)

    # Set the body using bytes and verify it's correctly assigned
    test_bytes = b"test body bytes"
    request.body = test_bytes
    assert request._body == test_bytes

    # Clean up is not necessary as the HTTPRequest instance is local to this test function
