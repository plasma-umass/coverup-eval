# file sanic/mixins/routes.py:41-159
# lines [41, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 74, 75, 77, 78, 80, 81, 83, 96, 99, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 114, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 133, 135, 136, 137, 139, 140, 141, 143, 144, 146, 147, 148, 151, 152, 154, 155, 157, 159]
# branches ['74->75', '74->77', '77->78', '77->80', '80->81', '80->83', '96->99', '96->101', '103->104', '103->105', '105->106', '105->114', '114->115', '114->117', '136->137', '136->143', '143->144', '143->151', '151->152', '151->154', '154->155', '154->157']

import pytest
from unittest.mock import Mock, patch
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @pytest.fixture
    def route_mixin(self):
        class TestClass(RouteMixin):
            def __init__(self):
                self._future_routes = set()
                self.strict_slashes = True
                self._apply_route = Mock()
                self._generate_name = Mock(return_value="test_handler")

        return TestClass()

    def test_route_decorator(self, route_mixin):
        @route_mixin.route("/test", methods=["GET"], host="localhost", strict_slashes=False, stream=True, version=1, name="test", ignore_body=True, apply=True, subprotocols=["sub1"], websocket=False, unquote=True, static=True)
        def test_handler(request):
            pass

        assert len(route_mixin._future_routes) == 1
        route = next(iter(route_mixin._future_routes))
        assert route.uri == "/test"
        assert route.methods == frozenset({"GET"})
        assert route.host == frozenset({"localhost"})
        assert route.strict_slashes is False
        assert route.stream is True
        assert route.version == 1
        assert route.name == "test_handler"
        assert route.ignore_body is True
        assert route.websocket is False
        assert route.subprotocols == frozenset({"sub1"})
        assert route.unquote is True
        assert route.static is True

        route_mixin._apply_route.assert_called_once_with(route)

    def test_route_decorator_missing_request_param(self, route_mixin):
        with pytest.raises(ValueError, match=r"Required parameter `request` missing in the test_handler\(\) route\?"):
            @route_mixin.route("/test")
            def test_handler():
                pass

    def test_route_decorator_missing_ws_param(self, route_mixin):
        with pytest.raises(ValueError, match=r"Required parameter `request` and/or `ws` missing in the test_handler\(\) route\?"):
            @route_mixin.route("/test", websocket=True)
            def test_handler(request):
                pass

    def test_route_decorator_handler_tuple(self, route_mixin):
        def handler(request):
            pass

        wrapped_handler = route_mixin.route("/test")(handler)
        assert wrapped_handler[1] == handler

        @route_mixin.route("/test")
        def test_handler(request):
            pass

        assert len(route_mixin._future_routes) == 2
        route = next(iter(route_mixin._future_routes))
        assert route.handler == handler

    def test_route_decorator_invalid_host(self, route_mixin):
        with pytest.raises(ValueError, match="Expected either string or Iterable of host strings"):
            @route_mixin.route("/test", host=123)
            def test_handler(request):
                pass

    def test_route_decorator_subprotocols(self, route_mixin):
        @route_mixin.route("/test", subprotocols={"sub1", "sub2"})
        def test_handler(request):
            pass

        assert len(route_mixin._future_routes) == 1
        route = next(iter(route_mixin._future_routes))
        assert route.subprotocols == frozenset({"sub1", "sub2"})
