# file sanic/exceptions.py:155-161
# lines [155, 156, 157, 161]
# branches []

import pytest
from sanic.exceptions import Forbidden, SanicException, add_status_code

# Assuming the add_status_code decorator is defined elsewhere in sanic.exceptions
# and works as expected, we will test the Forbidden exception class.

def test_forbidden_exception():
    # Test instantiation and status code
    exception = Forbidden("Forbidden access")
    assert exception.status_code == 403
    assert str(exception) == "Forbidden access"

    # Test inheritance from SanicException
    assert isinstance(exception, SanicException)

# This test function should cover the Forbidden class instantiation and confirm
# that the status code is correctly set to 403. It also checks that the
# exception message is correct and that Forbidden is a subclass of SanicException.
