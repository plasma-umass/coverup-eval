# file sanic/router.py:166-168
# lines [168]
# branches []

import pytest
from sanic.router import Router
from sanic import Sanic
from sanic.response import text

@pytest.fixture
def router():
    return Router()

def test_routes_static_property(router, mocker):
    # Setup: Create a mock Sanic app and add a static route to the router
    app = Sanic("test_app")
    app.router = router
    mocker.spy(router, 'add')

    @app.route('/test')
    def handler(request):
        return text('test')

    # Exercise: Access the routes_static property
    static_routes = router.routes_static

    # Verify: Check if the static_routes contains the added route
    assert len(static_routes) > 0
    router.add.assert_called_once()

    # Cleanup: No cleanup required as the router instance is unique to this test
