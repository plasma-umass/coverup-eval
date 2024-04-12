# file sanic/exceptions.py:54-62
# lines [54, 55, 56, 60, 61, 62]
# branches []

import pytest
from sanic.exceptions import MethodNotSupported

def test_method_not_supported_exception():
    message = "Method GET not allowed."
    method = "GET"
    allowed_methods = ["POST", "PUT"]

    try:
        raise MethodNotSupported(message, method, allowed_methods)
    except MethodNotSupported as e:
        assert str(e) == message
        assert e.status_code == 405
        assert e.headers == {"Allow": ", ".join(allowed_methods)}
