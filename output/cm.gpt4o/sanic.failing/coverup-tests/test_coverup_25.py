# file sanic/exceptions.py:177-223
# lines [177, 178, 179, 213, 214, 217, 218, 219, 221, 222]
# branches ['217->exit', '217->218']

import pytest
from sanic.exceptions import Unauthorized

def test_unauthorized_exception_with_basic_scheme():
    message = "Auth required."
    scheme = "Basic"
    realm = "Restricted Area"
    
    exc = Unauthorized(message, scheme=scheme, realm=realm)
    
    assert exc.status_code == 401
    assert exc.args[0] == message
    assert exc.headers["WWW-Authenticate"] == f"{scheme} realm=\"{realm}\""

def test_unauthorized_exception_with_digest_scheme():
    message = "Auth required."
    scheme = "Digest"
    realm = "Restricted Area"
    qop = "auth, auth-int"
    algorithm = "MD5"
    nonce = "abcdef"
    opaque = "zyxwvu"
    
    exc = Unauthorized(
        message, 
        scheme=scheme, 
        realm=realm, 
        qop=qop, 
        algorithm=algorithm, 
        nonce=nonce, 
        opaque=opaque
    )
    
    assert exc.status_code == 401
    assert exc.args[0] == message
    assert exc.headers["WWW-Authenticate"] == (
        f"{scheme} realm=\"{realm}\", qop=\"{qop}\", algorithm=\"{algorithm}\", "
        f"nonce=\"{nonce}\", opaque=\"{opaque}\""
    )

def test_unauthorized_exception_with_bearer_scheme():
    message = "Auth required."
    scheme = "Bearer"
    
    exc = Unauthorized(message, scheme=scheme)
    
    assert exc.status_code == 401
    assert exc.args[0] == message
    assert exc.headers["WWW-Authenticate"] == scheme

def test_unauthorized_exception_with_bearer_scheme_and_realm():
    message = "Auth required."
    scheme = "Bearer"
    realm = "Restricted Area"
    
    exc = Unauthorized(message, scheme=scheme, realm=realm)
    
    assert exc.status_code == 401
    assert exc.args[0] == message
    assert exc.headers["WWW-Authenticate"] == f"{scheme} realm=\"{realm}\""
