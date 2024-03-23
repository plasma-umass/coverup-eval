# file sanic/cookies.py:122-135
# lines [122, 135]
# branches []

import pytest
from sanic.cookies import Cookie

def test_cookie_encode():
    cookie = Cookie("key", "value")
    encoded_cookie = cookie.encode("utf-8")
    assert isinstance(encoded_cookie, bytes)
    assert encoded_cookie == str(cookie).encode("utf-8")

    with pytest.raises(UnicodeEncodeError):
        # This will cause a UnicodeEncodeError because the character
        # '\ud83d' cannot be encoded into 'ascii'
        cookie = Cookie("key", "\ud83d")
        cookie.encode("ascii")
