# file tornado/auth.py:76-77
# lines [76, 77]
# branches []

import pytest
from tornado.auth import AuthError

def test_auth_error():
    with pytest.raises(AuthError):
        raise AuthError("Authentication failed")

