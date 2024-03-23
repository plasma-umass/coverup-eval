# file sanic/mixins/routes.py:427-455
# lines [447, 448, 449, 450, 451, 452, 453, 454]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_route(mocker):
    mocker.patch.object(RouteMixin, 'route')

def test_delete_route_method(mock_route):
    app = Sanic("TestSanic")

    @app.delete("/test")
    async def handler(request):
        return text("delete")

    app.route.assert_called_once_with(
        "/test",
        methods=frozenset({"DELETE"}),
        host=None,
        strict_slashes=None,
        version=None,
        name=None,
        ignore_body=True,
    )
