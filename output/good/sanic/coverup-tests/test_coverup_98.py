# file sanic/mixins/middleware.py:14-46
# lines [29, 32, 33, 34, 35, 36, 39, 40, 41, 44, 45]
# branches ['34->35', '34->36', '39->40', '39->44']

import pytest
from sanic.mixins.middleware import MiddlewareMixin
from unittest.mock import MagicMock

class TestMiddlewareMixin:
    @pytest.fixture
    def mixin(self):
        mixin = MiddlewareMixin()
        mixin._future_middleware = []
        mixin._apply_middleware = MagicMock()
        return mixin

    def test_register_middleware_as_decorator(self, mixin):
        @mixin.middleware
        async def sample_middleware(request):
            pass

        assert sample_middleware in (mw.middleware for mw in mixin._future_middleware)
        mixin._apply_middleware.assert_called_once()

    def test_register_middleware_with_attach_to(self, mixin):
        @mixin.middleware('response')
        async def sample_middleware(request):
            pass

        assert sample_middleware in (mw.middleware for mw in mixin._future_middleware if mw.attach_to == 'response')
        mixin._apply_middleware.assert_called_once()

    def test_register_middleware_without_apply(self, mixin):
        async def sample_middleware(request):
            pass

        mixin.middleware(sample_middleware, apply=False)
        mixin._apply_middleware.assert_not_called()

    def test_register_middleware_callable(self, mixin):
        async def sample_middleware(request):
            pass

        registered_middleware = mixin.middleware(sample_middleware)
        assert registered_middleware == sample_middleware
        assert registered_middleware in (mw.middleware for mw in mixin._future_middleware)
        mixin._apply_middleware.assert_called_once()

    def test_register_middleware_partial(self, mixin):
        partial_middleware = mixin.middleware('response')
        assert callable(partial_middleware)

        @partial_middleware
        async def sample_middleware(request):
            pass

        assert sample_middleware in (mw.middleware for mw in mixin._future_middleware if mw.attach_to == 'response')
        mixin._apply_middleware.assert_called_once()
