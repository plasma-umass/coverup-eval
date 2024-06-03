# file sanic/mixins/middleware.py:11-12
# lines [11, 12]
# branches []

import pytest
from sanic.mixins.middleware import MiddlewareMixin

class MockFutureMiddleware:
    def __init__(self, handler, attach_to):
        self.handler = handler
        self.attach_to = attach_to

def test_apply_middleware_not_implemented():
    mixin = MiddlewareMixin()
    middleware = MockFutureMiddleware(lambda x: x, "request")

    with pytest.raises(NotImplementedError):
        mixin._apply_middleware(middleware)
