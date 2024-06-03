# file sanic/exceptions.py:155-161
# lines [155, 156, 157, 161]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

def test_forbidden_exception():
    @add_status_code(403)
    class Forbidden(SanicException):
        """
        **Status**: 403 Forbidden
        """
        pass

    # Create an instance of the Forbidden exception
    exception_instance = Forbidden("Access denied")

    # Assert that the status code is correctly set to 403
    assert exception_instance.status_code == 403

    # Assert that the message is correctly set
    assert str(exception_instance) == "Access denied"

    # Assert that the exception is an instance of SanicException
    assert isinstance(exception_instance, SanicException)
