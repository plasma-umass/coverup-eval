# file sanic/router.py:162-164
# lines [164]
# branches []

import pytest
from sanic.router import Router

class TestRouter(Router):
    def __init__(self, routes):
        self._routes = routes

    @property
    def routes(self):
        return self._routes

def test_routes_all_property():
    router = TestRouter(["route1", "route2", "route3"])
    
    assert router.routes_all == ["route1", "route2", "route3"]
