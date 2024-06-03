# file sanic/mixins/routes.py:387-425
# lines [387, 390, 391, 392, 393, 394, 417, 418, 419, 420, 421, 422, 423, 424]
# branches []

import pytest
from unittest.mock import Mock, patch

# Assuming RouteMixin is imported from the appropriate module
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'route')
    def test_patch_method(self, mock_route):
        # Create an instance of RouteMixin
        route_mixin = RouteMixin()

        # Define test parameters
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        stream = True
        version = 1
        name = "test_patch"

        # Call the patch method
        route_mixin.patch(uri, host, strict_slashes, stream, version, name)

        # Assert that the route method was called with the correct parameters
        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"PATCH"}),
            host=host,
            strict_slashes=strict_slashes,
            stream=stream,
            version=version,
            name=name,
        )
