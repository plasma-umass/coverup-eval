# file sanic/exceptions.py:177-223
# lines [177, 178, 179, 213, 214, 217, 218, 219, 221, 222]
# branches ['217->exit', '217->218']

import pytest
from sanic.exceptions import Unauthorized

def test_unauthorized_exception_with_scheme_and_params():
    message = "Auth required."
    scheme = "Digest"
    realm = "Restricted Area"
    qop = "auth, auth-int"
    algorithm = "MD5"
    nonce = "abcdef"
    opaque = "zyxwvu"

    with pytest.raises(Unauthorized) as exc_info:
        raise Unauthorized(
            message,
            scheme=scheme,
            realm=realm,
            qop=qop,
            algorithm=algorithm,
            nonce=nonce,
            opaque=opaque
        )

    exception = exc_info.value
    assert exception.status_code == 401
    assert exception.args[0] == message
    assert "WWW-Authenticate" in exception.headers
    assert exception.headers["WWW-Authenticate"] == (
        f"{scheme} realm=\"{realm}\", qop=\"{qop}\", algorithm=\"{algorithm}\", "
        f"nonce=\"{nonce}\", opaque=\"{opaque}\""
    )

def test_unauthorized_exception_without_scheme():
    message = "Auth required."

    with pytest.raises(Unauthorized) as exc_info:
        raise Unauthorized(message)

    exception = exc_info.value
    assert exception.status_code == 401
    assert exception.args[0] == message
    assert not hasattr(exception, 'headers') or "WWW-Authenticate" not in exception.headers
