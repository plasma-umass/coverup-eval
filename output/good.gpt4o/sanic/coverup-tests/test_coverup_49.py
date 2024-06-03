# file sanic/exceptions.py:105-115
# lines [105, 106, 107, 115]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_request_timeout_exception():
    @add_status_code(408)
    class RequestTimeout(SanicException):
        """The Web server (running the Web site) thinks that there has been too
        long an interval of time between 1) the establishment of an IP
        connection (socket) between the client and the server and
        2) the receipt of any data on that socket, so the server has dropped
        the connection. The socket connection has actually been lost - the Web
        server has 'timed out' on that particular socket connection.
        """
        pass

    # Create an instance of the exception
    exception_instance = RequestTimeout("Request timed out")

    # Assert that the status code is correctly set
    assert exception_instance.status_code == 408

    # Assert that the message is correctly set
    assert str(exception_instance) == "Request timed out"

    # Assert that the exception is an instance of SanicException
    assert isinstance(exception_instance, SanicException)
