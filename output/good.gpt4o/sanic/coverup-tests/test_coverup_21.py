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

            def _generate_name(self, name, handler):
                return name or handler.__name__

            def _apply_route(self, route):
                pass

        return TestClass()

    def test_route_decorator(self, route_mixin):
        @route_mixin.route('/test', methods=['GET'], host='localhost', strict_slashes=False, stream=True, version=1, name='test_route', ignore_body=True, apply=True, subprotocols=['sub1', 'sub2'], websocket=False, unquote=True, static=True)
        def handler(request):
            pass

        assert len(route_mixin._future_routes) == 1
        route = next(iter(route_mixin._future_routes))
        assert route.uri == '/test'
        assert route.methods == frozenset({'GET'})
        assert route.host == frozenset({'localhost'})
        assert route.strict_slashes == False
        assert route.stream == True
        assert route.version == 1
        assert route.name == 'test_route'
        assert route.ignore_body == True
        assert route.websocket == False
        assert route.subprotocols == frozenset({'sub1', 'sub2'})
        assert route.unquote == True
        assert route.static == True

    def test_route_decorator_missing_slash(self, route_mixin):
        @route_mixin.route('test')
        def handler(request):
            pass

        assert len(route_mixin._future_routes) == 1
        route = next(iter(route_mixin._future_routes))
        assert route.uri == '/test'

    def test_route_decorator_no_methods(self, route_mixin):
        @route_mixin.route('/test')
        def handler(request):
            pass

        assert len(route_mixin._future_routes) == 1
        route = next(iter(route_mixin._future_routes))
        assert route.methods == frozenset({'GET'})

    def test_route_decorator_invalid_host(self, route_mixin):
        with pytest.raises(ValueError):
            @route_mixin.route('/test', host=123)
            def handler(request):
                pass

    def test_route_decorator_invalid_websocket_handler(self, route_mixin):
        with pytest.raises(ValueError):
            @route_mixin.route('/test', websocket=True)
            def handler():
                pass

    def test_route_decorator_invalid_handler(self, route_mixin):
        with pytest.raises(ValueError):
            @route_mixin.route('/test')
            def handler():
                pass
