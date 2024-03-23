# file sanic/mixins/routes.py:221-249
# lines [221, 224, 225, 226, 227, 228, 241, 242, 243, 244, 245, 246, 247, 248]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_route(mocker):
    mocker.patch.object(RouteMixin, 'route')

def test_route_mixin_get(mock_route):
    app = Sanic("TestSanic")
    RouteMixin.get(app, uri="/test", host="example.com", strict_slashes=True, version=1, name="test_get", ignore_body=False)
    
    RouteMixin.route.assert_called_once_with(
        "/test",
        methods=frozenset({"GET"}),
        host="example.com",
        strict_slashes=True,
        version=1,
        name="test_get",
        ignore_body=False,
    )
