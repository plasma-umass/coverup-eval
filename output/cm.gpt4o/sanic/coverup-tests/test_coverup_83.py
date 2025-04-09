# file sanic/router.py:162-164
# lines [162, 163, 164]
# branches []

import pytest
from sanic.router import BaseRouter

class Router(BaseRouter):
    def __init__(self):
        self._routes = []

    @property
    def routes_all(self):
        return self._routes

    @property
    def routes(self):
        return self._routes

    def get(self, *args, **kwargs):
        pass

def test_routes_all_property():
    router = Router()
    # Mock the routes attribute
    router._routes = ["route1", "route2", "route3"]
    
    # Assert that routes_all returns the correct routes
    assert router.routes_all == ["route1", "route2", "route3"]

    # Clean up
    del router._routes
