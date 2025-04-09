# file sanic/mixins/middleware.py:7-7
# lines [7]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.middleware import MiddlewareMixin
from sanic.request import Request
from sanic.response import text

@pytest.mark.asyncio
async def test_middleware_mixin_execution():
    app = Sanic(__name__)
    mixin = MiddlewareMixin()

    # Define a simple middleware
    async def simple_middleware(request):
        return text("Middleware response")

    # Add the middleware to the mixin
    mixin.register_middleware(simple_middleware, "request")

    # Simulate a request middleware execution
    request = Request(b"/", {}, "", "1.1", None, app=app)
    response = await mixin._run_request_middleware(request, request.stream)

    # Assert that the middleware was executed and returned the correct response
    assert response.body == b"Middleware response"

    # Clean up
    mixin._request_middleware.clear()
