# file sanic/mixins/routes.py:387-425
# lines [387, 390, 391, 392, 393, 394, 417, 418, 419, 420, 421, 422, 423, 424]
# branches []

import pytest
from unittest.mock import Mock, patch

# Assuming the RouteMixin class is in a module named sanic.mixins.routes
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'route')
    def test_patch_method(self, mock_route):
        mixin = RouteMixin()
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        stream = True
        version = 1
        name = "test_patch"

        mixin.patch(uri, host, strict_slashes, stream, version, name)

        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"PATCH"}),
            host=host,
            strict_slashes=strict_slashes,
            stream=stream,
            version=version,
            name=name,
        )
