# file sanic/exceptions.py:135-143
# lines [135, 136, 137, 141, 142, 143]
# branches []

import pytest
from sanic.exceptions import ContentRangeError

class ContentRangeMock:
    total = 1000

@pytest.fixture
def content_range_mock():
    return ContentRangeMock()

def test_content_range_error(content_range_mock):
    message = "Range Not Satisfiable"
    exception = ContentRangeError(message, content_range_mock)
    
    assert exception.status_code == 416
    assert str(exception) == message
    assert exception.headers == {"Content-Range": "bytes */1000"}

