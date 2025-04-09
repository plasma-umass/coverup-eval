# file sanic/mixins/middleware.py:48-52
# lines [48, 49, 50, 52]
# branches ['49->50', '49->52']

import pytest
from sanic.mixins.middleware import MiddlewareMixin
from unittest.mock import Mock

# Test function to cover the missing lines/branches
def test_on_request_with_callable_middleware():
    mixin = MiddlewareMixin()
    mixin.middleware = Mock()

    # Define a callable middleware function
    def test_middleware(request):
        pass

    # Call on_request with a callable middleware
    mixin.on_request(test_middleware)

    # Assert that mixin.middleware was called with the correct arguments
    mixin.middleware.assert_called_once_with(test_middleware, "request")

def test_on_request_with_non_callable_middleware(mocker):
    mixin = MiddlewareMixin()
    mocker.patch.object(mixin, 'middleware')

    # Call on_request with a non-callable middleware (None in this case)
    partial_function = mixin.on_request(None)

    # Assert that the returned value is a partial function
    assert callable(partial_function), "The returned object should be callable"
    assert partial_function.func == mixin.middleware, "The partial function should wrap the middleware method"
    assert partial_function.keywords == {'attach_to': 'request'}, "The partial function should have 'request' as the attach_to keyword"

# Run the tests
def test_middleware_mixin():
    test_on_request_with_callable_middleware()
    test_on_request_with_non_callable_middleware(mocker=Mock())
