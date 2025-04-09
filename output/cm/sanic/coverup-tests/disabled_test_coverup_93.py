# file sanic/mixins/routes.py:387-425
# lines [417, 418, 419, 420, 421, 422, 423, 424]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_route(mocker):
    mocker.patch.object(RouteMixin, 'route')

def test_patch_method(mock_route):
    app = Sanic("TestApp")
    RouteMixin.patch(app, uri="/test", host="example.com", strict_slashes=True, stream=True, version=1, name="test_patch")

    RouteMixin.route.assert_called_once_with(
        "/test",
        methods=frozenset({"PATCH"}),
        host="example.com",
        strict_slashes=True,
        stream=True,
        version=1,
        name="test_patch"
    )
