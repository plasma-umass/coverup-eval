# file sanic/mixins/middleware.py:14-46
# lines []
# branches ['34->36']

import pytest
from unittest.mock import MagicMock, patch
from sanic.mixins.middleware import MiddlewareMixin

class TestMiddlewareMixin:
    @pytest.fixture
    def middleware_mixin(self):
        class App(MiddlewareMixin):
            def __init__(self):
                self._future_middleware = []
                self._apply_middleware = MagicMock()

        return App()

    def test_middleware_apply_true(self, middleware_mixin):
        def sample_middleware(request):
            pass
        
        middleware_mixin.middleware(sample_middleware, apply=True)

        assert len(middleware_mixin._future_middleware) == 1
        middleware_mixin._apply_middleware.assert_called_once_with(middleware_mixin._future_middleware[0])

    def test_middleware_apply_false(self, middleware_mixin):
        def sample_middleware(request):
            pass
        
        middleware_mixin.middleware(sample_middleware, apply=False)

        assert len(middleware_mixin._future_middleware) == 1
        middleware_mixin._apply_middleware.assert_not_called()
