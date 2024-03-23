# file sanic/mixins/routes.py:457-489
# lines [457, 460, 461, 462, 463, 464, 465, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_app(mocker):
    app = mocker.Mock(spec=Sanic)
    app.route = mocker.Mock()
    return app

def test_websocket_route_decorator(mock_app):
    # Create a mock websocket handler
    @RouteMixin.websocket(mock_app, '/ws', host='example.com', strict_slashes=True, subprotocols=['chat', 'superchat'], version=1, name='test_ws')
    async def mock_ws_handler(request, ws):
        await ws.send('Hello, WebSocket!')

    # Assert that the route decorator was called with the correct parameters
    mock_app.route.assert_called_once_with(
        uri='/ws',
        host='example.com',
        methods=None,
        strict_slashes=True,
        version=1,
        name='test_ws',
        apply=True,
        subprotocols=['chat', 'superchat'],
        websocket=True
    )
