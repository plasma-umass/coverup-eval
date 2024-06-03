# file sanic/mixins/routes.py:35-36
# lines [35, 36]
# branches []

import pytest
from sanic.mixins.routes import RouteMixin

def test_apply_route_not_implemented():
    route_mixin = RouteMixin()
    with pytest.raises(NotImplementedError):
        route_mixin._apply_route(None)
