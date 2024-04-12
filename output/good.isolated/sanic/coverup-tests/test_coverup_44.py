# file sanic/exceptions.py:45-51
# lines [45, 46, 47, 51]
# branches []

import pytest
from sanic.exceptions import SanicException, add_status_code

# Define the InvalidUsage exception with the add_status_code decorator
@add_status_code(400)
class InvalidUsage(SanicException):
    """
    **Status**: 400 Bad Request
    """
    pass

# Define the test function
def test_invalid_usage_exception():
    # Test that the InvalidUsage exception has the correct status code
    exception = InvalidUsage("Invalid usage test")
    assert exception.status_code == 400

# Run the test function if this file is executed directly (not recommended for pytest)
if __name__ == "__main__":
    pytest.main()
