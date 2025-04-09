# file tornado/httpclient.py:690-729
# lines [690, 691, 711, 714, 715, 717, 718, 719, 720, 722, 723, 729]
# branches []

import pytest
from tornado.httpclient import HTTPClientError, HTTPResponse
from unittest import mock

def test_http_client_error():
    # Mocking HTTPResponse
    mock_response = mock.Mock(spec=HTTPResponse)
    mock_response.code = 404
    mock_response.body = b"Not Found"
    
    # Creating an instance of HTTPClientError
    error = HTTPClientError(404, "Not Found", mock_response)
    
    # Assertions to verify the attributes
    assert error.code == 404
    assert error.message == "Not Found"
    assert error.response == mock_response
    assert str(error) == "HTTP 404: Not Found"
    assert repr(error) == "HTTP 404: Not Found"
    
    # Clean up
    del error
    del mock_response
