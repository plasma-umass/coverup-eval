# file sanic/response.py:60-79
# lines [60, 61, 77, 78, 79]
# branches ['77->78', '77->79']

import pytest
from sanic.response import BaseHTTPResponse
from sanic.cookies import CookieJar

@pytest.fixture
def response():
    return BaseHTTPResponse()

def test_base_http_response_cookies(response):
    # Access the cookies property when it is None, it should create a new CookieJar
    assert response._cookies is None, "Initially, response._cookies should be None"
    cookies = response.cookies
    assert isinstance(cookies, CookieJar), "response.cookies should return a CookieJar instance"
    assert response._cookies is cookies, "response._cookies should be set to the CookieJar instance after first access"

    # Set a cookie and verify it is in the CookieJar
    response.cookies["test"] = "It worked!"
    assert "test" in response.cookies, "The 'test' cookie should be set in the cookies"
    assert response.cookies["test"].value == "It worked!", "The 'test' cookie should have the correct value"

    # Set cookie attributes and verify they are set correctly
    response.cookies["test"]["domain"] = ".yummy-yummy-cookie.com"
    response.cookies["test"]["httponly"] = True
    assert response.cookies["test"]["domain"] == ".yummy-yummy-cookie.com", "The 'test' cookie domain should be set correctly"
    assert response.cookies["test"]["httponly"] is True, "The 'test' cookie httponly should be set to True"

    # Access the cookies property again, it should return the existing CookieJar
    assert response.cookies is cookies, "Subsequent access to response.cookies should return the existing CookieJar instance"
