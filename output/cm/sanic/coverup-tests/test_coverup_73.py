# file sanic/mixins/middleware.py:8-9
# lines [8, 9]
# branches []

import pytest
from sanic.mixins.middleware import MiddlewareMixin

class TestMiddlewareMixin:
    def test_middleware_mixin_initialization(self):
        mixin = MiddlewareMixin()
        assert hasattr(mixin, '_future_middleware')
        assert isinstance(mixin._future_middleware, list)
        assert len(mixin._future_middleware) == 0
