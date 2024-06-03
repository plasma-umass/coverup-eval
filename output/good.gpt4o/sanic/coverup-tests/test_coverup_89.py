# file sanic/router.py:170-172
# lines [172]
# branches []

import pytest
from sanic.router import Router

def test_routes_dynamic_property():
    router = Router()
    router.dynamic_routes = ["route1", "route2"]

    assert router.routes_dynamic == ["route1", "route2"]
