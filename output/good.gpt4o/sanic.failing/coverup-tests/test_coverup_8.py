# file sanic/mixins/routes.py:349-385
# lines [349, 352, 353, 354, 355, 356, 377, 378, 379, 380, 381, 382, 383, 384]
# branches []

import pytest
from unittest.mock import Mock, patch
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @patch.object(RouteMixin, 'route')
    def test_options(self, mock_route):
        mixin = RouteMixin()
        uri = "/test"
        host = "localhost"
        strict_slashes = True
        version = 1
        name = "test_route"
        ignore_body = False

        mixin.options(uri, host, strict_slashes, version, name, ignore_body)

        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"OPTIONS"}),
            host=host,
            strict_slashes=strict_slashes,
            version=version,
            name=name,
            ignore_body=ignore_body,
        )
