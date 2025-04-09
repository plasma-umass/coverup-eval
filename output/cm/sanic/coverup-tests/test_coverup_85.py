# file sanic/mixins/routes.py:38-39
# lines [38, 39]
# branches []

import pytest
from sanic.mixins.routes import RouteMixin
from sanic.exceptions import NotFound

class MockRouteMixin(RouteMixin):
    def _apply_static(self, static) -> None:
        super()._apply_static(static)

def test_route_mixin_apply_static():
    mock_route_mixin = MockRouteMixin()

    with pytest.raises(NotImplementedError):
        mock_route_mixin._apply_static(None)
