# file sanic/mixins/middleware.py:7-7
# lines [7]
# branches []

import pytest
from sanic.mixins.middleware import MiddlewareMixin

class TestMiddlewareMixin:
    @pytest.fixture
    def middleware_mixin(self):
        return MiddlewareMixin()

    def test_middleware_mixin_initialization(self, middleware_mixin):
        assert middleware_mixin is not None

    def test_middleware_mixin_add_middleware(self, middleware_mixin, mocker):
        mock_middleware = mocker.Mock()
        if not hasattr(middleware_mixin, '_middlewares'):
            middleware_mixin._middlewares = []
        middleware_mixin._middlewares.append(mock_middleware)
        assert mock_middleware in middleware_mixin._middlewares

    def test_middleware_mixin_remove_middleware(self, middleware_mixin, mocker):
        mock_middleware = mocker.Mock()
        if not hasattr(middleware_mixin, '_middlewares'):
            middleware_mixin._middlewares = []
        middleware_mixin._middlewares.append(mock_middleware)
        middleware_mixin._middlewares.remove(mock_middleware)
        assert mock_middleware not in middleware_mixin._middlewares

    def test_middleware_mixin_execute_middleware(self, middleware_mixin, mocker):
        mock_middleware = mocker.Mock()
        if not hasattr(middleware_mixin, '_middlewares'):
            middleware_mixin._middlewares = []
        middleware_mixin._middlewares.append(mock_middleware)
        for middleware in middleware_mixin._middlewares:
            middleware()
        mock_middleware.assert_called_once()
