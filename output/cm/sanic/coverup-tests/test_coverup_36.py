# file sanic/exceptions.py:146-152
# lines [146, 147, 148, 152]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

# Assuming the above code is in a file named sanic/exceptions.py
# and we are creating a new test file named test_exceptions.py

# test_exceptions.py

def test_header_expectation_failed():
    @add_status_code(417)
    class TestHeaderExpectationFailed(SanicException):
        pass

    exception_instance = TestHeaderExpectationFailed("Expectation Failed")
    assert exception_instance.status_code == 417
    assert str(exception_instance) == "Expectation Failed"
