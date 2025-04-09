# file sanic/mixins/middleware.py:14-46
# lines [29, 32, 33, 34, 35, 36, 39, 40, 41, 44, 45]
# branches ['34->35', '34->36', '39->40', '39->44']

import pytest
from unittest.mock import MagicMock, patch
from sanic.mixins.middleware import MiddlewareMixin
from functools import partial

class FutureMiddleware:
    def __init__(self, middleware, attach_to):
        self.middleware = middleware
        self.attach_to = attach_to

    def __eq__(self, other):
        return (
            self.middleware == other.middleware and
            self.attach_to == other.attach_to
        )

class TestMiddlewareMixin:
    @pytest.fixture
    def middleware_mixin(self):
        class App(MiddlewareMixin):
            def __init__(self):
                self._future_middleware = []
                self._apply_middleware = MagicMock()

        return App()

    def test_register_middleware_callable(self, middleware_mixin):
        def sample_middleware(request):
            pass

        middleware_mixin.middleware(sample_middleware)

        assert len(middleware_mixin._future_middleware) == 1
        assert middleware_mixin._future_middleware[0] == FutureMiddleware(sample_middleware, 'request')
        middleware_mixin._apply_middleware.assert_called_once()

    def test_register_middleware_partial(self, middleware_mixin):
        def sample_middleware(request):
            pass

        partial_middleware = middleware_mixin.middleware('response')
        assert isinstance(partial_middleware, partial)

        partial_middleware(sample_middleware)

        assert len(middleware_mixin._future_middleware) == 1
        assert middleware_mixin._future_middleware[0] == FutureMiddleware(sample_middleware, 'response')
        middleware_mixin._apply_middleware.assert_called_once()
