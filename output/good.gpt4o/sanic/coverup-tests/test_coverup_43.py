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

    # Create an instance of the ServerError
    error_instance = ServerError("Internal Server Error")

    # Assert that the status code is correctly set to 500
    assert error_instance.status_code == 500

    # Assert that the message is correctly set
    assert str(error_instance) == "Internal Server Error"
