# file sanic/mixins/routes.py:251-279
# lines [251, 254, 255, 256, 257, 258, 271, 272, 273, 274, 275, 276, 277, 278]
# branches []

import pytest
from unittest.mock import Mock, patch
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'route')
    def test_post_method(self, mock_route):
        # Arrange
        mixin = RouteMixin()
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        stream = True
        version = 1
        name = "test_route"

        # Act
        mixin.post(uri, host, strict_slashes, stream, version, name)

        # Assert
        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"POST"}),
            host=host,
            strict_slashes=strict_slashes,
            stream=stream,
            version=version,
            name=name,
        )
