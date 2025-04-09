# file tornado/httpclient.py:680-683
# lines [682, 683]
# branches ['682->exit', '682->683']

import pytest
from tornado.httpclient import HTTPResponse, HTTPError, HTTPRequest

@pytest.fixture
def mock_response():
    # Create a mock HTTPResponse with an error
    request = HTTPRequest(url='http://example.com')
    response = HTTPResponse(request, 500, reason='Internal Server Error')
    response.error = HTTPError(500, "Internal Server Error")
    return response

def test_httpresponse_rethrow(mock_response):
    # Verify that the rethrow method raises the error
    with pytest.raises(HTTPError) as exc_info:
        mock_response.rethrow()
    
    assert exc_info.value.code == 500
    assert str(exc_info.value) == "HTTP 500: Internal Server Error"
