# file tornado/httpclient.py:629-669
# lines [661, 662]
# branches ['660->661']

import pytest
from tornado.httpclient import HTTPResponse, HTTPRequest, HTTPError
from io import BytesIO

@pytest.fixture
def mock_request():
    return HTTPRequest(url='http://example.com')

@pytest.fixture
def mock_headers():
    return {'Content-Type': 'text/plain'}

def test_http_response_error_is_response_code(mock_request, mock_headers):
    # Create a response with a status code that should trigger the error
    response = HTTPResponse(
        request=mock_request,
        code=404,
        headers=mock_headers,
        buffer=BytesIO(b'Not Found'),
        reason='Not Found'
    )

    # Assert that the error is an instance of HTTPError
    assert isinstance(response.error, HTTPError)
    # Assert that the error's code is the same as the response's code
    assert response.error.code == 404
    # Assert that the error's message is the same as the response's reason
    assert response.error.message == 'Not Found'
    # Assert that the error's response is the response itself
    assert response.error.response is response
    # Assert that the _error_is_response_code flag is set to True
    assert response._error_is_response_code is True
