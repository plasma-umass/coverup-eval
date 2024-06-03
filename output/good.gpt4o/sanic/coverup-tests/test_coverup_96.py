# file sanic/mixins/routes.py:221-249
# lines [241, 242, 243, 244, 245, 246, 247, 248]
# branches []

import pytest
from unittest.mock import Mock, patch
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'route')
    def test_get_method(self, mock_route):
        # Arrange
        mixin = RouteMixin()
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        version = 1
        name = "test_route"
        ignore_body = False

        # Act
        mixin.get(uri, host, strict_slashes, version, name, ignore_body)

        # Assert
        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"GET"}),
            host=host,
            strict_slashes=strict_slashes,
            version=version,
            name=name,
            ignore_body=ignore_body,
        )
