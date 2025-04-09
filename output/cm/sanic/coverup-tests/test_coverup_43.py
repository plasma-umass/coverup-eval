# file sanic/router.py:174-176
# lines [174, 175, 176]
# branches []

import pytest
from sanic.router import Router

@pytest.fixture
def router():
    return Router()

def test_routes_regex_property(router):
    # Set up a mock regex_routes attribute
    mock_regex_routes = "mock_regex_routes"
    router.regex_routes = mock_regex_routes

    # Test the routes_regex property
    assert router.routes_regex == mock_regex_routes

    # Clean up by deleting the mock attribute
    del router.regex_routes
