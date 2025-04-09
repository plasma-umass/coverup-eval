# file sanic/exceptions.py:65-71
# lines [65, 66, 67, 71]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_server_error():
    @add_status_code(500)
    class ServerError(SanicException):
        """
        **Status**: 500 Internal Server Error
        """
        pass

    error_instance = ServerError("Internal Server Error")
    assert error_instance.status_code == 500
    assert str(error_instance) == "Internal Server Error"
