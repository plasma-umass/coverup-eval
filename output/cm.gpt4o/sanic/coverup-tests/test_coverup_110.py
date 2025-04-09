# file sanic/mixins/routes.py:161-218
# lines [203, 204]
# branches ['202->203', '206->209']

import pytest
from sanic.mixins.routes import RouteMixin
from sanic.views import CompositionView

class MockHandler:
    is_stream = True

class MockCompositionView(CompositionView):
    def __init__(self):
        super().__init__()
        self.handlers = {
            "GET": MockHandler,
            "POST": MockHandler,
        }

@pytest.fixture
def route_mixin():
    class TestRouteMixin(RouteMixin):
        def __init__(self):
            self.strict_slashes = True

        def route(self, *args, **kwargs):
            return lambda x: x

    return TestRouteMixin()

def test_add_route_composition_view(route_mixin):
    handler = MockCompositionView()
    route_mixin.add_route(handler, "/test")

    assert handler.handlers["GET"].is_stream

def test_add_route_strict_slashes_none(route_mixin):
    handler = lambda x: x
    route_mixin.add_route(handler, "/test", strict_slashes=None)

    assert route_mixin.strict_slashes is True
