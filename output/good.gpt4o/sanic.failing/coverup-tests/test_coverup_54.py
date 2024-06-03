# file sanic/cookies.py:137-156
# lines [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 154, 156]
# branches ['140->141', '140->156', '141->142', '141->146', '146->147', '146->151', '151->152', '151->154']

import pytest
from datetime import datetime, timedelta
from sanic.cookies import Cookie

def _quote(value):
    return '"{}"'.format(value)

@pytest.fixture
def mock_quote(mocker):
    return mocker.patch('sanic.cookies._quote', side_effect=_quote)

def test_cookie_str(mock_quote):
    class TestCookie(Cookie):
        _keys = {
            "max-age": "Max-Age",
            "expires": "Expires",
            "path": "Path",
            "domain": "Domain",
            "secure": "Secure",
            "httponly": "HttpOnly",
            "samesite": "SameSite"
        }
        _flags = {"secure", "httponly"}

    cookie = TestCookie(key="test", value="value")
    cookie["max-age"] = 3600
    cookie["expires"] = datetime.utcnow() + timedelta(days=1)
    cookie["path"] = "/"
    cookie["domain"] = "example.com"
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["samesite"] = "Lax"

    result = str(cookie)
    assert 'test="value"' in result
    assert 'Max-Age=3600' in result
    assert 'Expires=' in result
    assert 'Path=/' in result
    assert 'Domain=example.com' in result
    assert 'Secure' in result
    assert 'HttpOnly' in result
    assert 'SameSite=Lax' in result

    # Test TypeError branch for max-age
    with pytest.raises(ValueError, match="Cookie max-age must be an integer"):
        cookie["max-age"] = "invalid"

    # Test cleanup
    del cookie["max-age"]
    del cookie["expires"]
    del cookie["path"]
    del cookie["domain"]
    del cookie["secure"]
    del cookie["httponly"]
    del cookie["samesite"]
    assert "max-age" not in cookie
    assert "expires" not in cookie
    assert "path" not in cookie
    assert "domain" not in cookie
    assert "secure" not in cookie
    assert "httponly" not in cookie
    assert "samesite" not in cookie
