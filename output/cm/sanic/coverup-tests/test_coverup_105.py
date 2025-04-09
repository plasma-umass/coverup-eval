# file sanic/mixins/routes.py:35-36
# lines [36]
# branches []

import pytest
from sanic.mixins.routes import RouteMixin

class TestRouteMixin(RouteMixin):
    pass

def test_route_mixin_apply_route_not_implemented_error():
    route_mixin = TestRouteMixin()
    with pytest.raises(NotImplementedError):
        route_mixin._apply_route(None)
