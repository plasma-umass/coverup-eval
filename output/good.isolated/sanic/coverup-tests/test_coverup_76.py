# file sanic/exceptions.py:105-115
# lines [105, 106, 107, 115]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

# Assuming the RequestTimeout class is defined in sanic.exceptions as provided in the prompt
# and that the add_status_code decorator is also defined there.

# Define the RequestTimeout exception class with the decorator applied
@add_status_code(408)
class RequestTimeout(SanicException):
    pass

# Define the test function
def test_request_timeout_exception():
    # Instantiate the exception
    exception = RequestTimeout("Request timed out")

    # Assert that the exception message is correct
    assert str(exception) == "Request timed out"

    # Assert that the status code is set correctly by the decorator
    assert exception.status_code == 408

# Run the test function if this file is executed directly (not recommended for pytest)
if __name__ == "__main__":
    pytest.main()
