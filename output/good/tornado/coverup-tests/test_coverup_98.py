# file tornado/simple_httpclient.py:60-76
# lines [60, 61, 72, 73, 75, 76]
# branches []

import pytest
from tornado.simple_httpclient import HTTPStreamClosedError

def test_http_stream_closed_error():
    message = "Test stream closed"
    error = HTTPStreamClosedError(message)
    
    # Verify the error code and message
    assert error.code == 599
    assert str(error) == message
    
    # Test with no message
    error_no_message = HTTPStreamClosedError("")
    assert str(error_no_message) == "Unknown"

    # Clean up is not necessary as no external resources are being used
