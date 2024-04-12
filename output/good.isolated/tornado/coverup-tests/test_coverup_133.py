# file tornado/httpclient.py:685-687
# lines [685, 686, 687]
# branches []

import pytest
from tornado.httpclient import HTTPResponse, HTTPRequest

@pytest.fixture
def http_response():
    # Setup the HTTPResponse object with some test data
    request = HTTPRequest(url='http://example.com')
    response = HTTPResponse(request, 200, reason='OK', headers={}, buffer=None)
    response.test_attribute = "test_value"
    yield response
    # No teardown needed as the object will be garbage collected

def test_http_response_repr(http_response):
    # Test the __repr__ method of HTTPResponse
    expected_repr_start = "HTTPResponse("
    actual_repr = repr(http_response)
    assert actual_repr.startswith(expected_repr_start), "HTTPResponse __repr__ does not start with expected value"
    assert "test_attribute='test_value'" in actual_repr, "HTTPResponse __repr__ does not contain the test attribute"
