# file sanic/cookies.py:108-120
# lines [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 120]
# branches ['109->110', '109->111', '111->exit', '111->112', '112->113', '112->115', '113->114', '113->120', '115->116', '115->120', '116->117', '116->120']

import pytest
from datetime import datetime
from sanic.cookies import Cookie

def test_cookie_setitem_invalid_key():
    cookie = Cookie("test", "value")
    with pytest.raises(KeyError, match="Unknown cookie property"):
        cookie["invalid_key"] = "value"

def test_cookie_setitem_max_age_non_integer():
    cookie = Cookie("test", "value")
    cookie._keys = ["max-age"]
    with pytest.raises(ValueError, match="Cookie max-age must be an integer"):
        cookie["max-age"] = "non-integer"

def test_cookie_setitem_expires_non_datetime():
    cookie = Cookie("test", "value")
    cookie._keys = ["expires"]
    with pytest.raises(TypeError, match="Cookie 'expires' property must be a datetime"):
        cookie["expires"] = "non-datetime"

def test_cookie_setitem_valid_max_age():
    cookie = Cookie("test", "value")
    cookie._keys = ["max-age"]
    cookie["max-age"] = 3600
    assert cookie["max-age"] == 3600

def test_cookie_setitem_valid_expires():
    cookie = Cookie("test", "value")
    cookie._keys = ["expires"]
    expires_time = datetime.now()
    cookie["expires"] = expires_time
    assert cookie["expires"] == expires_time
