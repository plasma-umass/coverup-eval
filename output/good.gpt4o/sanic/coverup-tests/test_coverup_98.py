# file sanic/exceptions.py:177-223
# lines [214, 217, 218, 219, 221, 222]
# branches ['217->exit', '217->218']

import pytest
from sanic.exceptions import Unauthorized

def test_unauthorized_with_scheme_and_realm():
    message = "Auth required."
    scheme = "Basic"
    realm = "Restricted Area"
    
    exc = Unauthorized(message, scheme=scheme, realm=realm)
    
    assert exc.status_code == 401
    assert exc.headers["WWW-Authenticate"] == f"{scheme} realm=\"{realm}\""

def test_unauthorized_with_scheme_and_multiple_kwargs():
    message = "Auth required."
    scheme = "Digest"
    kwargs = {
        "realm": "Restricted Area",
        "qop": "auth, auth-int",
        "algorithm": "MD5",
        "nonce": "abcdef",
        "opaque": "zyxwvu"
    }
    
    exc = Unauthorized(message, scheme=scheme, **kwargs)
    
    assert exc.status_code == 401
    expected_challenge = ', '.join([f'{k}="{v}"' for k, v in kwargs.items()])
    assert exc.headers["WWW-Authenticate"] == f"{scheme} {expected_challenge}"

def test_unauthorized_with_scheme_but_no_realm():
    message = "Auth required."
    scheme = "Bearer"
    
    exc = Unauthorized(message, scheme=scheme)
    
    assert exc.status_code == 401
    assert exc.headers["WWW-Authenticate"] == f"{scheme}"

def test_unauthorized_without_scheme():
    message = "Auth required."
    
    exc = Unauthorized(message)
    
    assert exc.status_code == 401
    assert not hasattr(exc, 'headers')
