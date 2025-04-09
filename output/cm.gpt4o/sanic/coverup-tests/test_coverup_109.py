# file sanic/mixins/routes.py:41-159
# lines [99]
# branches ['96->99', '154->157']

import pytest
from unittest.mock import Mock
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @pytest.fixture
    def route_mixin(self):
        class App(RouteMixin):
            def __init__(self):
                self._future_routes = set()
                self.strict_slashes = True
                self._apply_route = Mock()

            def _generate_name(self, name, handler):
                return name or handler.__name__

        return App()

    def test_route_decorator_with_tuple_handler(self, route_mixin):
        def handler_fn(request):
            pass

        handler_tuple = (None, handler_fn)
        decorator = route_mixin.route("/test", apply=False)
        route, handler = decorator(handler_tuple)

        assert handler is handler_fn
        assert route.handler is handler_fn
        assert route.uri == "/test"
        assert route_mixin._apply_route.call_count == 0

    def test_route_decorator_with_apply(self, route_mixin):
        def handler_fn(request):
            pass

        decorator = route_mixin.route("/test", apply=True)
        route, handler = decorator(handler_fn)

        assert handler is handler_fn
        assert route.handler is handler_fn
        assert route.uri == "/test"
        route_mixin._apply_route.assert_called_once_with(route)
