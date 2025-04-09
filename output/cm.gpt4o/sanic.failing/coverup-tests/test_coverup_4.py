# file sanic/mixins/routes.py:427-455
# lines [427, 430, 431, 432, 433, 434, 447, 448, 449, 450, 451, 452, 453, 454]
# branches []

import pytest
from unittest.mock import Mock, patch
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'route')
    def test_delete_method(self, mock_route):
        # Arrange
        mixin = RouteMixin()
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        version = 1
        name = "test_delete"
        ignore_body = False

        # Act
        mixin.delete(uri, host, strict_slashes, version, name, ignore_body)

        # Assert
        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"DELETE"}),
            host=host,
            strict_slashes=strict_slashes,
            version=version,
            name=name,
            ignore_body=ignore_body,
        )
