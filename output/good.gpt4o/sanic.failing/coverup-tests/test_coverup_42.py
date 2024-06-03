# file sanic/exceptions.py:36-42
# lines [36, 37, 38, 42]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_not_found_exception():
    @add_status_code(404)
    class NotFound(SanicException):
        """
        **Status**: 404 Not Found
        """
        pass

    # Create an instance of the NotFound exception
    exception_instance = NotFound("Resource not found")

    # Assert that the status code is correctly set to 404
    assert exception_instance.status_code == 404

    # Assert that the message is correctly set
    assert str(exception_instance) == "Resource not found"

    # Assert that the exception is an instance of SanicException
    assert isinstance(exception_instance, SanicException)

    # Assert that the exception is an instance of NotFound
    assert isinstance(exception_instance, NotFound)
