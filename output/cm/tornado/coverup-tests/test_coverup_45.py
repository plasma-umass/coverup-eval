# file tornado/httpclient.py:690-729
# lines [690, 691, 711, 714, 715, 717, 718, 719, 720, 722, 723, 729]
# branches []

import pytest
from tornado.httpclient import HTTPClientError
from tornado.httputil import responses

def test_http_client_error():
    # Test the case where message is provided
    error_with_message = HTTPClientError(404, "Not Found")
    assert error_with_message.code == 404
    assert error_with_message.message == "Not Found"
    assert error_with_message.response is None
    assert str(error_with_message) == "HTTP 404: Not Found"
    assert repr(error_with_message) == "HTTP 404: Not Found"

    # Test the case where message is not provided and code is known
    error_without_message_known_code = HTTPClientError(404)
    assert error_without_message_known_code.code == 404
    assert error_without_message_known_code.message == responses[404]
    assert error_without_message_known_code.response is None
    assert str(error_without_message_known_code) == f"HTTP 404: {responses[404]}"
    assert repr(error_without_message_known_code) == f"HTTP 404: {responses[404]}"

    # Test the case where message is not provided and code is unknown
    unknown_code = 999
    error_without_message_unknown_code = HTTPClientError(unknown_code)
    assert error_without_message_unknown_code.code == unknown_code
    assert error_without_message_unknown_code.message == "Unknown"
    assert error_without_message_unknown_code.response is None
    assert str(error_without_message_unknown_code) == "HTTP 999: Unknown"
    assert repr(error_without_message_unknown_code) == "HTTP 999: Unknown"

@pytest.fixture
def mock_http_response(mocker):
    return mocker.Mock()

def test_http_client_error_with_response(mock_http_response):
    # Test the case where response is provided
    error_with_response = HTTPClientError(500, "Server Error", mock_http_response)
    assert error_with_response.code == 500
    assert error_with_response.message == "Server Error"
    assert error_with_response.response is mock_http_response
    assert str(error_with_response) == "HTTP 500: Server Error"
    assert repr(error_with_response) == "HTTP 500: Server Error"
