# file tornado/auth.py:76-77
# lines [76, 77]
# branches []

import pytest
from tornado.auth import AuthError

def test_auth_error():
    # Test that AuthError can be raised and caught as expected
    with pytest.raises(AuthError):
        raise AuthError("An authentication error occurred")

    # Test that AuthError is a subclass of Exception
    assert issubclass(AuthError, Exception)

    # Test that AuthError instance contains the correct message
    try:
        raise AuthError("Custom error message")
    except AuthError as e:
        assert str(e) == "Custom error message"
