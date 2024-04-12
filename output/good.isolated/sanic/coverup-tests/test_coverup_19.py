# file sanic/mixins/routes.py:349-385
# lines [349, 352, 353, 354, 355, 356, 377, 378, 379, 380, 381, 382, 383, 384]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_route(mocker):
    mocker.patch.object(RouteMixin, 'route', return_value='route_decorator')

def test_options_method(mock_route):
    app = Sanic("test_sanic_app")
    RouteMixin.options(app, uri="/test")

    RouteMixin.route.assert_called_once_with(
        "/test",
        methods=frozenset({"OPTIONS"}),
        host=None,
        strict_slashes=None,
        version=None,
        name=None,
        ignore_body=True,
    )

    assert RouteMixin.route(app, "/test", methods=frozenset({"OPTIONS"})) == 'route_decorator'
