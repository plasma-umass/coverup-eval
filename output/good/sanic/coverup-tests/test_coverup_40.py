# file sanic/exceptions.py:74-83
# lines [74, 75, 76, 83]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

# Assuming the provided code is part of the sanic.exceptions module
# and we are extending the test suite for that module.

# First, we need to define the exception with the decorator as provided
@add_status_code(503)
class ServiceUnavailable(SanicException):
    """
    **Status**: 503 Service Unavailable

    The server is currently unavailable (because it is overloaded or
    down for maintenance). Generally, this is a temporary state.
    """
    pass

# Now, we write a test function to cover the ServiceUnavailable exception
def test_service_unavailable_exception():
    with pytest.raises(ServiceUnavailable) as exc_info:
        raise ServiceUnavailable("Service is down")

    assert exc_info.value.status_code == 503
    assert str(exc_info.value) == "Service is down"

# Run the test with pytest
# Note: This test script is meant to be part of a test suite and should be run using pytest.
# It is not a standalone script and does not include code to invoke pytest.main().
