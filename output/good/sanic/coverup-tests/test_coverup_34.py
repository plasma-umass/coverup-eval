# file sanic/exceptions.py:36-42
# lines [36, 37, 38, 42]
# branches []

import pytest
from sanic.exceptions import NotFound, SanicException, add_status_code

# Assuming the add_status_code decorator is defined elsewhere in sanic.exceptions
# and works as expected, adding a status_code attribute to the exception class.

def test_not_found_exception():
    # Test to ensure the NotFound exception is correctly instantiated and has a 404 status code.
    try:
        raise NotFound("Page not found")
    except NotFound as e:
        assert str(e) == "Page not found"
        assert e.status_code == 404
