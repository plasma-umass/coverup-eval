# file sanic/mixins/routes.py:457-489
# lines [457, 460, 461, 462, 463, 464, 465, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488]
# branches []

import pytest
from unittest.mock import Mock, patch

# Assuming the RouteMixin class is in a module named sanic.mixins.routes
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch('sanic.mixins.routes.RouteMixin.route')
    def test_websocket(self, mock_route):
        mixin = RouteMixin()
        
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        subprotocols = ["protocol1", "protocol2"]
        version = 1
        name = "test_websocket"
        apply = True

        mixin.websocket(
            uri=uri,
            host=host,
            strict_slashes=strict_slashes,
            subprotocols=subprotocols,
            version=version,
            name=name,
            apply=apply,
        )

        mock_route.assert_called_once_with(
            uri=uri,
            host=host,
            methods=None,
            strict_slashes=strict_slashes,
            version=version,
            name=name,
            apply=apply,
            subprotocols=subprotocols,
            websocket=True,
        )
