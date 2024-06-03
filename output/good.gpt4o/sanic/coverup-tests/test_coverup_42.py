# file sanic/exceptions.py:45-51
# lines [45, 46, 47, 51]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_invalid_usage_exception():
    @add_status_code(400)
    class InvalidUsage(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    try:
        raise InvalidUsage("This is an invalid usage error")
    except InvalidUsage as e:
        assert e.status_code == 400
        assert str(e) == "This is an invalid usage error"
