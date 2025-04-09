# file sanic/exceptions.py:177-223
# lines [177, 178, 179, 213, 214, 217, 218, 219, 221, 222]
# branches ['217->exit', '217->218']

import pytest
from sanic.exceptions import SanicException, add_status_code

@add_status_code(401)
class Unauthorized(SanicException):
    """
    **Status**: 401 Unauthorized

    :param message: Message describing the exception.
    :param status_code: HTTP Status code.
    :param scheme: Name of the authentication scheme to be used.

    When present, kwargs is used to complete the WWW-Authentication header.

    Examples::

        # With a Basic auth-scheme, realm MUST be present:
        raise Unauthorized("Auth required.",
                           scheme="Basic",
                           realm="Restricted Area")

        # With a Digest auth-scheme, things are a bit more complicated:
        raise Unauthorized("Auth required.",
                           scheme="Digest",
                           realm="Restricted Area",
                           qop="auth, auth-int",
                           algorithm="MD5",
                           nonce="abcdef",
                           opaque="zyxwvu")

        # With a Bearer auth-scheme, realm is optional so you can write:
        raise Unauthorized("Auth required.", scheme="Bearer")

        # or, if you want to specify the realm:
        raise Unauthorized("Auth required.",
                           scheme="Bearer",
                           realm="Restricted Area")
    """

    def __init__(self, message, status_code=None, scheme=None, **kwargs):
        super().__init__(message, status_code)

        # if auth-scheme is specified, set "WWW-Authenticate" header
        if scheme is not None:
            values = ['{!s}="{!s}"'.format(k, v) for k, v in kwargs.items()]
            challenge = ", ".join(values)

            self.headers = {
                "WWW-Authenticate": f"{scheme} {challenge}".rstrip()
            }

def test_unauthorized_basic_scheme():
    exc = Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    assert exc.status_code == 401
    assert exc.headers["WWW-Authenticate"] == 'Basic realm="Restricted Area"'

def test_unauthorized_digest_scheme():
    exc = Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    assert exc.status_code == 401
    assert exc.headers["WWW-Authenticate"] == 'Digest realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu"'

def test_unauthorized_bearer_scheme():
    exc = Unauthorized("Auth required.", scheme="Bearer")
    assert exc.status_code == 401
    assert exc.headers["WWW-Authenticate"] == 'Bearer'

def test_unauthorized_bearer_scheme_with_realm():
    exc = Unauthorized("Auth required.", scheme="Bearer", realm="Restricted Area")
    assert exc.status_code == 401
    assert exc.headers["WWW-Authenticate"] == 'Bearer realm="Restricted Area"'

def test_unauthorized_no_scheme():
    exc = Unauthorized("Auth required.")
    assert exc.status_code == 401
    assert not hasattr(exc, 'headers')
