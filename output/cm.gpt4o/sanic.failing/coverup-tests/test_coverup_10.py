# file sanic/mixins/routes.py:457-489
# lines [457, 460, 461, 462, 463, 464, 465, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488]
# branches []

import pytest
from unittest.mock import Mock, patch
from typing import Optional, List

# Assuming the RouteMixin class is defined in sanic/mixins/routes.py
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @pytest.fixture
    def route_mixin(self):
        return RouteMixin()

    @patch.object(RouteMixin, 'route')
    def test_websocket(self, mock_route, route_mixin):
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        subprotocols = ["protocol1", "protocol2"]
        version = 1
        name = "test_websocket"
        apply = True

        # Call the websocket method
        route_mixin.websocket(
            uri=uri,
            host=host,
            strict_slashes=strict_slashes,
            subprotocols=subprotocols,
            version=version,
            name=name,
            apply=apply,
        )

        # Assert that the route method was called with the correct parameters
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
