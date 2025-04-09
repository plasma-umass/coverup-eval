# file sanic/mixins/routes.py:491-525
# lines [491, 495, 496, 497, 498, 499, 518, 519, 520, 521, 522, 523, 524, 525]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the RouteMixin class is part of the sanic.mixins.routes module
from sanic.mixins.routes import RouteMixin

# Mock the websocket decorator to verify it's called with correct parameters
def mock_websocket_decorator(*args, **kwargs):
    def decorator(f):
        f.decorated = True
        return f
    return decorator

@pytest.fixture
def route_mixin(mocker):
    mixin = RouteMixin()
    mocker.patch.object(mixin, 'websocket', side_effect=mock_websocket_decorator)
    return mixin

def test_add_websocket_route(route_mixin):
    # Define a simple handler function
    async def handler(request, ws):
        pass

    # Call the add_websocket_route method with test parameters
    uri = '/test'
    host = 'localhost'
    strict_slashes = True
    subprotocols = ['chat', 'superchat']
    version = 1
    name = 'test_websocket'

    decorated_handler = route_mixin.add_websocket_route(
        handler,
        uri=uri,
        host=host,
        strict_slashes=strict_slashes,
        subprotocols=subprotocols,
        version=version,
        name=name
    )

    # Assert that the handler is decorated
    assert hasattr(decorated_handler, 'decorated')
    assert decorated_handler.decorated is True

    # Assert that the websocket decorator was called with the correct parameters
    route_mixin.websocket.assert_called_once_with(
        uri=uri,
        host=host,
        strict_slashes=strict_slashes,
        subprotocols=subprotocols,
        version=version,
        name=name
    )
