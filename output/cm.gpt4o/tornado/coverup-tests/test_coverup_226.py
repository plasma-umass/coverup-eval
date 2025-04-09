# file tornado/httpclient.py:685-687
# lines [686, 687]
# branches []

import pytest
from tornado.httpclient import HTTPResponse

def test_httpresponse_repr():
    class MockHTTPResponse(HTTPResponse):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    response = MockHTTPResponse(status_code=200, reason="OK", body="response body")
    repr_str = repr(response)
    
    assert repr_str.startswith("MockHTTPResponse(")
    assert "status_code=200" in repr_str
    assert "reason='OK'" in repr_str
    assert "body='response body'" in repr_str
