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

    try:
        raise ServiceUnavailable("Service is temporarily unavailable")
    except ServiceUnavailable as e:
        assert e.status_code == 503
        assert str(e) == "Service is temporarily unavailable"
