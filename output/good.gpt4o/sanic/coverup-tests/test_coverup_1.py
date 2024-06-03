# file sanic/mixins/routes.py:281-309
# lines [281, 284, 285, 286, 287, 288, 301, 302, 303, 304, 305, 306, 307, 308]
# branches []

import pytest
from unittest.mock import Mock, patch
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'route')
    def test_put_method(self, mock_route):
        # Arrange
        mixin = RouteMixin()
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        stream = True
        version = 1
        name = "test_put"

        # Act
        mixin.put(uri, host, strict_slashes, stream, version, name)

        # Assert
        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"PUT"}),
            host=host,
            strict_slashes=strict_slashes,
            stream=stream,
            version=version,
            name=name,
        )
