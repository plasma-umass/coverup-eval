# file sanic/mixins/routes.py:29-33
# lines [29, 30, 31, 32, 33]
# branches []

import pytest
from sanic.mixins.routes import RouteMixin

def test_route_mixin_initialization():
    route_mixin = RouteMixin()
    
    assert isinstance(route_mixin._future_routes, set)
    assert isinstance(route_mixin._future_statics, set)
    assert route_mixin.name == ""
    assert route_mixin.strict_slashes is False
