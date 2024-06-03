# file sanic/exceptions.py:135-143
# lines [135, 136, 137, 141, 142, 143]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

@add_status_code(416)
class ContentRangeError(SanicException):
    """
    **Status**: 416 Range Not Satisfiable
    """
    def __init__(self, message, content_range):
        super().__init__(message)
        self.headers = {"Content-Range": f"bytes */{content_range.total}"}

class MockContentRange:
    def __init__(self, total):
        self.total = total

def test_content_range_error():
    message = "Range Not Satisfiable"
    content_range = MockContentRange(total=1000)
    
    exception = ContentRangeError(message, content_range)
    
    assert exception.status_code == 416
    assert exception.args[0] == message
    assert exception.headers == {"Content-Range": "bytes */1000"}
