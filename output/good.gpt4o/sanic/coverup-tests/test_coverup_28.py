# file sanic/exceptions.py:54-62
# lines [54, 55, 56, 60, 61, 62]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

@add_status_code(405)
class MethodNotSupported(SanicException):
    """
    **Status**: 405 Method Not Allowed
    """
    def __init__(self, message, method, allowed_methods):
        super().__init__(message)
        self.headers = {"Allow": ", ".join(allowed_methods)}

def test_method_not_supported():
    message = "Method not allowed"
    method = "POST"
    allowed_methods = ["GET", "HEAD", "OPTIONS"]
    
    exception = MethodNotSupported(message, method, allowed_methods)
    
    assert exception.status_code == 405
    assert exception.args[0] == message
    assert exception.headers == {"Allow": "GET, HEAD, OPTIONS"}
