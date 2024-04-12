# file sanic/mixins/routes.py:29-33
# lines [29, 30, 31, 32, 33]
# branches []

import pytest
from sanic.mixins.routes import RouteMixin

@pytest.fixture
def route_mixin_instance():
    return RouteMixin()

def test_route_mixin_initialization(route_mixin_instance):
    assert isinstance(route_mixin_instance._future_routes, set)
    assert isinstance(route_mixin_instance._future_statics, set)
    assert route_mixin_instance.name == ""
    assert route_mixin_instance.strict_slashes is False
