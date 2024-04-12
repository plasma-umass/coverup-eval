# file sanic/mixins/middleware.py:54-58
# lines [54, 55, 56, 58]
# branches ['55->56', '55->58']

import pytest
from sanic.mixins.middleware import MiddlewareMixin
from functools import partial

# Mocking a Sanic app that includes the MiddlewareMixin
class MockSanicApp(MiddlewareMixin):
    def __init__(self):
        self._response_middleware = []

    def middleware(self, middleware, attach_to=None):
        if attach_to == "response":
            self._response_middleware.append(middleware)
            return middleware

# Test function to check if the on_response method correctly handles a callable middleware
def test_on_response_with_callable_middleware():
    app = MockSanicApp()

    @app.on_response
    def my_middleware(request):
        pass

    assert my_middleware in app._response_middleware

# Test function to check if the on_response method correctly returns a partial when no callable is provided
def test_on_response_without_callable_middleware():
    app = MockSanicApp()

    middleware_decorator = app.on_response()
    assert isinstance(middleware_decorator, partial)
    assert middleware_decorator.func == app.middleware
    assert middleware_decorator.keywords == {'attach_to': 'response'}

    @middleware_decorator
    def another_middleware(request):
        pass

    assert another_middleware in app._response_middleware
