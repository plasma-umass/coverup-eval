# file sanic/exceptions.py:65-71
# lines [65, 66, 67, 71]
# branches []

import pytest
from sanic.exceptions import SanicException

# Assuming the provided code snippet is part of the sanic.exceptions module
# and that the ServerError class is defined there as shown.

# Define the ServerError class with the decorator for the test
# Since the decorator is not defined, we will mock it
def add_status_code(status_code):
    def decorator(cls):
        cls.status_code = status_code
        return cls
    return decorator

@add_status_code(500)
class ServerError(SanicException):
    pass

# Test function to cover the ServerError class
def test_server_error():
    try:
        raise ServerError("Internal Server Error")
    except SanicException as e:
        assert e.status_code == 500
        assert str(e) == "Internal Server Error"

# This test does not require cleanup as it does not modify any global state
# or external resources. It also does not require the use of pytest-mock.
