# file sanic/mixins/routes.py:349-385
# lines [377, 378, 379, 380, 381, 382, 383, 384]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_route(mocker):
    mocker.patch.object(RouteMixin, 'route')

def test_options_method_route_mixin(mock_route):
    app = Sanic("TestApp")
    app.options("/test", host="example.com", strict_slashes=True, version=1, name="test_options", ignore_body=False)

    RouteMixin.route.assert_called_once_with(
        "/test",
        methods=frozenset({"OPTIONS"}),
        host="example.com",
        strict_slashes=True,
        version=1,
        name="test_options",
        ignore_body=False,
    )
