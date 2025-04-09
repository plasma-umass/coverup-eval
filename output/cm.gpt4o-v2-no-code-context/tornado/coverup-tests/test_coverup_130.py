# file: tornado/auth.py:76-77
# asked: {"lines": [76, 77], "branches": []}
# gained: {"lines": [76, 77], "branches": []}

import pytest
from tornado.auth import AuthError

def test_auth_error():
    with pytest.raises(AuthError):
        raise AuthError("This is a test error")

def test_auth_error_message():
    try:
        raise AuthError("This is a test error")
    except AuthError as e:
        assert str(e) == "This is a test error"
