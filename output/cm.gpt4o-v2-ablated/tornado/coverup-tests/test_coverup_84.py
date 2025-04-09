# file: tornado/auth.py:76-77
# asked: {"lines": [76, 77], "branches": []}
# gained: {"lines": [76, 77], "branches": []}

import pytest
from tornado.auth import AuthError

def test_auth_error_inheritance():
    with pytest.raises(AuthError):
        raise AuthError("Authentication failed")

    assert issubclass(AuthError, Exception)
