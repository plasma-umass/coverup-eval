# file sanic/mixins/routes.py:311-347
# lines [311, 314, 315, 316, 317, 318, 339, 340, 341, 342, 343, 344, 345, 346]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_route(mocker):
    mocker.patch.object(RouteMixin, 'route')

def test_route_mixin_head(mock_route):
    app = Sanic("test_sanic_app")
    RouteMixin.head(app, uri="/test", host="example.com", strict_slashes=True, version=1, name="test_head_route", ignore_body=False)
    
    RouteMixin.route.assert_called_once_with(
        "/test",
        methods=frozenset({"HEAD"}),
        host="example.com",
        strict_slashes=True,
        version=1,
        name="test_head_route",
        ignore_body=False,
    )
