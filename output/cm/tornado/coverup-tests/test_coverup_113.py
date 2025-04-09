# file tornado/httpclient.py:565-567
# lines [565, 566, 567]
# branches []

import pytest
from tornado.httpclient import HTTPRequest

@pytest.fixture
def http_request():
    request = HTTPRequest(url='http://example.com')
    request._body = b'test_body'
    yield request
    # No cleanup needed for this simple object

def test_http_request_body_property(http_request):
    assert http_request.body == b'test_body', "The body property should return the correct bytes"
