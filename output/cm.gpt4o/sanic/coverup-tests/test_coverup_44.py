# file sanic/exceptions.py:74-83
# lines [74, 75, 76, 83]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_service_unavailable_exception():
    @add_status_code(503)
    class ServiceUnavailable(SanicException):
        """
        **Status**: 503 Service Unavailable

        The server is currently unavailable (because it is overloaded or
        down for maintenance). Generally, this is a temporary state.
        """
        pass

    # Instantiate the exception
    exc = ServiceUnavailable("Service is temporarily unavailable")

    # Assertions to verify the status code and message
    assert exc.status_code == 503
    assert str(exc) == "Service is temporarily unavailable"
