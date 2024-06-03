# file sanic/mixins/routes.py:491-525
# lines [491, 495, 496, 497, 498, 499, 518, 519, 520, 521, 522, 523, 524, 525]
# branches []

import pytest
from unittest.mock import Mock, patch

# Assuming the RouteMixin class is in a module named sanic.mixins.routes
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'websocket')
    def test_add_websocket_route(self, mock_websocket):
        # Arrange
        mixin = RouteMixin()
        handler = Mock()
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        subprotocols = ["protocol1", "protocol2"]
        version = 1
        name = "test_route"

        # Act
        result = mixin.add_websocket_route(
            handler=handler,
            uri=uri,
            host=host,
            strict_slashes=strict_slashes,
            subprotocols=subprotocols,
            version=version,
            name=name,
        )

        # Assert
        mock_websocket.assert_called_once_with(
            uri=uri,
            host=host,
            strict_slashes=strict_slashes,
            subprotocols=subprotocols,
            version=version,
            name=name,
        )
        mock_websocket.return_value.assert_called_once_with(handler)
        assert result == mock_websocket.return_value(handler)
