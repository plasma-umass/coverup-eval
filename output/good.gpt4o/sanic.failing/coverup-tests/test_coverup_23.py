# file sanic/cookies.py:83-98
# lines [83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97]
# branches []

import pytest
from sanic.cookies import Cookie

def test_cookie_initialization():
    cookie = Cookie("test_key", "test_value")
    assert isinstance(cookie, dict)
    assert hasattr(cookie, '_keys')
    assert hasattr(cookie, '_flags')

def test_cookie_keys():
    cookie = Cookie("test_key", "test_value")
    expected_keys = {
        "expires": "expires",
        "path": "Path",
        "comment": "Comment",
        "domain": "Domain",
        "max-age": "Max-Age",
        "secure": "Secure",
        "httponly": "HttpOnly",
        "version": "Version",
        "samesite": "SameSite",
    }
    assert cookie._keys == expected_keys

def test_cookie_flags():
    cookie = Cookie("test_key", "test_value")
    expected_flags = {"secure", "httponly"}
    assert cookie._flags == expected_flags
