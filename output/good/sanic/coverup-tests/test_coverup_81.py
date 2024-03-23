# file sanic/exceptions.py:164-169
# lines [164, 165, 169]
# branches []

import pytest
from sanic.exceptions import InvalidRangeType

class MockContentRange:
    total = 1000

def test_invalid_range_type():
    with pytest.raises(InvalidRangeType) as exc_info:
        raise InvalidRangeType("Invalid range type", content_range=MockContentRange())

    assert exc_info.type is InvalidRangeType
    assert str(exc_info.value) == "Invalid range type"
    assert exc_info.value.headers == {"Content-Range": "bytes */1000"}
