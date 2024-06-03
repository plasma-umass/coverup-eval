# file sanic/mixins/routes.py:161-218
# lines [188, 189, 191, 192, 193, 194, 195, 196, 199, 200, 201, 202, 203, 204, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218]
# branches ['188->189', '188->199', '191->192', '191->199', '193->191', '193->194', '195->191', '195->196', '199->200', '199->206', '201->202', '201->206', '202->201', '202->203', '206->207', '206->209']

import pytest
from sanic.mixins.routes import RouteMixin
from sanic.views import HTTPMethodView, CompositionView
from unittest.mock import Mock

class TestRouteMixin(RouteMixin):
    def route(self, *args, **kwargs):
        def wrapper(handler):
            return handler
        return wrapper

@pytest.fixture
def route_mixin():
    return TestRouteMixin()

def test_add_route_http_method_view(route_mixin):
    class TestView(HTTPMethodView):
        def get(self, request):
            pass
        def post(self, request):
            pass

    handler = TestView.as_view()
    route_mixin.add_route(handler, '/test')

    assert hasattr(handler, 'view_class')
    assert handler.view_class.get
    assert handler.view_class.post

def test_add_route_composition_view(route_mixin):
    handler = CompositionView()
    handler.add(['GET'], lambda request: None)
    handler.add(['POST'], lambda request: None)

    route_mixin.add_route(handler, '/test')

    assert isinstance(handler, CompositionView)
    assert 'GET' in handler.handlers
    assert 'POST' in handler.handlers

def test_add_route_strict_slashes_none(route_mixin, mocker):
    mocker.patch.object(route_mixin, 'strict_slashes', True)
    handler = Mock()
    route_mixin.add_route(handler, '/test')

    assert route_mixin.strict_slashes is True

def test_add_route_with_stream(route_mixin):
    class TestView(HTTPMethodView):
        def get(self, request):
            pass
        def post(self, request):
            pass

    handler = TestView.as_view()
    handler.view_class.get.is_stream = True
    route_mixin.add_route(handler, '/test')

    assert hasattr(handler.view_class.get, 'is_stream')
    assert handler.view_class.get.is_stream is True
