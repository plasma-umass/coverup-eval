# file sanic/mixins/routes.py:281-309
# lines [281, 284, 285, 286, 287, 288, 301, 302, 303, 304, 305, 306, 307, 308]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_route(mocker):
    mocker.patch.object(RouteMixin, 'route')

def test_put_method_route_mixin(mock_route):
    app = Sanic("TestApp")
    RouteMixin.put(app, uri="/test_put", host="example.com", strict_slashes=True, stream=True, version=1, name="test_put_route")
    
    RouteMixin.route.assert_called_once_with(
        "/test_put",
        methods=frozenset({"PUT"}),
        host="example.com",
        strict_slashes=True,
        stream=True,
        version=1,
        name="test_put_route"
    )
