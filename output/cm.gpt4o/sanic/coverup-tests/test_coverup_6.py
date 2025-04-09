# file sanic/mixins/routes.py:311-347
# lines [311, 314, 315, 316, 317, 318, 339, 340, 341, 342, 343, 344, 345, 346]
# branches []

import pytest
from unittest.mock import Mock, patch
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'route')
    def test_head_method(self, mock_route):
        # Arrange
        mixin = RouteMixin()
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        version = 1
        name = "test_route"
        ignore_body = False

        # Act
        mixin.head(uri, host, strict_slashes, version, name, ignore_body)

        # Assert
        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"HEAD"}),
            host=host,
            strict_slashes=strict_slashes,
            version=version,
            name=name,
            ignore_body=ignore_body,
        )
