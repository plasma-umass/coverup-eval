# file sanic/response.py:60-79
# lines [60, 61, 77, 78, 79]
# branches ['77->78', '77->79']

import pytest
from sanic.response import BaseHTTPResponse
from sanic.cookies import CookieJar

class MockBaseHTTPResponse(BaseHTTPResponse):
    def __init__(self):
        self._cookies = None
        self.headers = {}

@pytest.fixture
def mock_response():
    return MockBaseHTTPResponse()

def test_cookies_property(mock_response):
    # Ensure that the cookies property initializes the CookieJar if _cookies is None
    assert mock_response._cookies is None
    cookies = mock_response.cookies
    assert isinstance(cookies, CookieJar)
    assert mock_response._cookies is cookies

    # Ensure that the cookies property returns the existing CookieJar if _cookies is not None
    existing_cookies = mock_response._cookies
    cookies_again = mock_response.cookies
    assert cookies_again is existing_cookies

    # Clean up
    mock_response._cookies = None
    mock_response.headers = {}
