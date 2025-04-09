# file sanic/cookies.py:137-156
# lines [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 154, 156]
# branches ['140->141', '140->156', '141->142', '141->146', '146->147', '146->151', '151->152', '151->154']

import pytest
from sanic.cookies import Cookie
from datetime import datetime, timedelta

@pytest.fixture
def mock_cookie():
    cookie = Cookie(key="test", value="value")
    cookie._keys = {"max-age": "Max-Age", "expires": "Expires", "httponly": "HttpOnly", "domain": "Domain"}
    cookie._flags = {"httponly": True}
    return cookie

def test_cookie_str_with_max_age_as_int(mock_cookie):
    mock_cookie["max-age"] = 300
    assert str(mock_cookie) == "test=value; Max-Age=300"

def test_cookie_str_with_max_age_as_non_int(mock_cookie):
    mock_cookie._keys["max-age"] = "Max-Age"
    mock_cookie["max-age"] = "300"  # Assuming the implementation allows string digits
    assert str(mock_cookie) == "test=value; Max-Age=300"

def test_cookie_str_with_expires(mock_cookie):
    expires_time = datetime.utcnow() + timedelta(days=1)
    mock_cookie["expires"] = expires_time
    expected_date_str = expires_time.strftime("%a, %d-%b-%Y %T GMT")
    assert f"Expires={expected_date_str}" in str(mock_cookie)

def test_cookie_str_with_flag(mock_cookie):
    mock_cookie["httponly"] = True
    assert "HttpOnly" in str(mock_cookie)

def test_cookie_str_with_non_flag_non_special_key(mock_cookie):
    mock_cookie["domain"] = "example.com"
    assert "Domain=example.com" in str(mock_cookie)
