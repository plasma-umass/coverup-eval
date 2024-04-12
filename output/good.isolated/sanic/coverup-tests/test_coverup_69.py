# file sanic/mixins/middleware.py:11-12
# lines [11, 12]
# branches []

import pytest
from sanic.mixins.middleware import MiddlewareMixin
from sanic.exceptions import SanicException

class TestMiddlewareMixin(MiddlewareMixin):
    def _apply_middleware(self, middleware):
        super()._apply_middleware(middleware)

def test_middleware_mixin_apply_not_implemented():
    mixin = TestMiddlewareMixin()
    with pytest.raises(NotImplementedError):
        mixin._apply_middleware(None)
