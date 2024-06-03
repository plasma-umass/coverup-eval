# file sanic/exceptions.py:164-169
# lines [164, 165, 169]
# branches []

import pytest
from sanic.exceptions import ContentRangeError

def test_invalid_range_type():
    class InvalidRangeType(ContentRangeError):
        """
        **Status**: 416 Range Not Satisfiable
        """
        pass

    # Mock content_range object with a total attribute
    class MockContentRange:
        total = 1234

    # Create an instance of the InvalidRangeType exception
    exception_instance = InvalidRangeType("Invalid range type", MockContentRange())

    # Assert that the exception instance is indeed an instance of InvalidRangeType
    assert isinstance(exception_instance, InvalidRangeType)

    # Assert that the exception instance is also an instance of ContentRangeError
    assert isinstance(exception_instance, ContentRangeError)

    # Assert that the message is correctly set
    assert str(exception_instance) == "Invalid range type"

    # Assert that the headers are correctly set
    assert exception_instance.headers == {"Content-Range": "bytes */1234"}
