# file sanic/router.py:20-28
# lines [20, 21, 26, 27]
# branches []

import pytest
from sanic.router import Router
from sanic.request import Request
from sanic.response import text
from sanic.exceptions import NotFound, MethodNotSupported
from sanic.constants import HTTP_METHODS

@pytest.mark.asyncio
async def test_router_methods_coverage():
    router = Router()
    handler = lambda request: text('OK')
    router.add('/test', handler, methods=['GET'])

    # Test the default method
    request = Request(b'/', {}, '1.1', 'GET', None)
    route, _ = router.get(request)
    assert route.handler == handler

    # Test allowed methods
    for method in HTTP_METHODS:
        if method != 'GET':  # We already added 'GET' above
            router.add('/test', handler, methods=[method])
            request = Request(b'/', {}, '1.1', method, None)
            route, _ = router.get(request)
            assert route.handler == handler

    # Test method not allowed
    with pytest.raises(MethodNotSupported):
        request = Request(b'/', {}, '1.1', 'INVALID', None)
        router.get(request)

    # Test route not found
    with pytest.raises(NotFound):
        request = Request(b'/', {}, '1.1', 'GET', None)
        router.get(request)
