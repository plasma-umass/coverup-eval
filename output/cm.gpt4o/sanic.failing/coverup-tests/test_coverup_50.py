# file sanic/mixins/routes.py:161-218
# lines [161, 165, 166, 167, 168, 169, 170, 188, 189, 191, 192, 193, 194, 195, 196, 199, 200, 201, 202, 203, 204, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218]
# branches ['188->189', '188->199', '191->192', '191->199', '193->191', '193->194', '195->191', '195->196', '199->200', '199->206', '201->202', '201->206', '202->201', '202->203', '206->207', '206->209']

import pytest
from sanic.mixins.routes import RouteMixin
from sanic.views import HTTPMethodView, CompositionView
from unittest.mock import Mock

class TestRouteMixin(RouteMixin):
    def route(self, uri, methods, host, strict_slashes, stream, version, name):
        def wrapper(handler):
            return handler
        return wrapper

@pytest.fixture
def route_mixin():
    return TestRouteMixin()

def test_add_route_with_http_method_view(route_mixin):
    class MyView(HTTPMethodView):
        def get(self, request):
            return "GET"
        def post(self, request):
            return "POST"
    
    handler = MyView.as_view()
    route_mixin.add_route(handler, "/test", methods=["GET", "POST"])
    assert hasattr(handler, "view_class")

def test_add_route_with_composition_view(route_mixin):
    handler_get = Mock()
    handler_post = Mock()
    handler_get.is_stream = True

    view = CompositionView()
    view.add(["GET"], handler_get)
    view.add(["POST"], handler_post)

    route_mixin.add_route(view, "/test")
    assert isinstance(view, CompositionView)
    assert "GET" in view.handlers
    assert "POST" in view.handlers

def test_add_route_with_defaults(route_mixin):
    handler = Mock()
    route_mixin.strict_slashes = True

    route_mixin.add_route(handler, "/test")
    handler.assert_not_called()
