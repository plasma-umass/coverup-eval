# file sanic/exceptions.py:54-62
# lines [61, 62]
# branches []

import pytest
from sanic.exceptions import MethodNotSupported

def test_method_not_supported():
    message = "Method not allowed"
    method = "POST"
    allowed_methods = ["GET", "POST", "PUT"]

    exception = MethodNotSupported(message, method, allowed_methods)

    assert exception.status_code == 405
    assert exception.args[0] == message
    assert exception.headers == {"Allow": "GET, POST, PUT"}
