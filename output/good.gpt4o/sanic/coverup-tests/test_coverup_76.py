# file sanic/mixins/routes.py:38-39
# lines [38, 39]
# branches []

import pytest
from sanic.mixins.routes import RouteMixin

def test_apply_static_raises_not_implemented_error():
    route_mixin = RouteMixin()
    with pytest.raises(NotImplementedError):
        route_mixin._apply_static(None)
