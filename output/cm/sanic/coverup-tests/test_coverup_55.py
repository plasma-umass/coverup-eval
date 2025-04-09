# file sanic/router.py:170-172
# lines [170, 171, 172]
# branches []

import pytest
from sanic.router import Router

@pytest.fixture
def router():
    return Router()

def test_routes_dynamic_property(router):
    # Setup: Ensure that dynamic_routes is an empty dictionary initially
    assert router.dynamic_routes == {}

    # Test: Access the routes_dynamic property
    dynamic_routes = router.routes_dynamic

    # Verify: Check if the property access returns the correct value
    assert dynamic_routes == router.dynamic_routes

    # Cleanup: No cleanup required as no state change occurs outside the scope of the test
