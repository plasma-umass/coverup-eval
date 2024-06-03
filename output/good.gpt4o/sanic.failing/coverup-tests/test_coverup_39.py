# file sanic/exceptions.py:45-51
# lines [45, 46, 47, 51]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_invalid_usage_status_code():
    @add_status_code(400)
    class InvalidUsage(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    exception_instance = InvalidUsage("Invalid usage")
    assert exception_instance.status_code == 400
    assert str(exception_instance) == "Invalid usage"
