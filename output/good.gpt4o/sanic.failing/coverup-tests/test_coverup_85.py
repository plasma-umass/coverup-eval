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

    # Create a mock content_range object with a 'total' attribute
    class MockContentRange:
        total = 1234

    # Create an instance of the InvalidRangeType exception with required arguments
    exception_instance = InvalidRangeType("Invalid range type", MockContentRange())

    # Assert that the exception is an instance of ContentRangeError
    assert isinstance(exception_instance, ContentRangeError)

    # Assert that the exception message is correct
    assert str(exception_instance) == "Invalid range type"

    # Assert that the headers are set correctly
    assert exception_instance.headers == {"Content-Range": "bytes */1234"}
