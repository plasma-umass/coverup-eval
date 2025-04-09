# file sanic/mixins/routes.py:251-279
# lines [251, 254, 255, 256, 257, 258, 271, 272, 273, 274, 275, 276, 277, 278]
# branches []

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from sanic.response import text

@pytest.fixture
def mock_app(mocker):
    app = mocker.MagicMock(spec=Sanic)
    app.route = mocker.MagicMock(return_value=lambda x: x)
    return app

def test_route_mixin_post(mock_app):
    mixin = RouteMixin()
    mixin.route = mock_app.route

    @mixin.post('/test', host='example.com', strict_slashes=True, version=1, name='test_post')
    async def handler(request):
        return text('test')

    mock_app.route.assert_called_once_with(
        '/test',
        methods=frozenset({'POST'}),
        host='example.com',
        strict_slashes=True,
        stream=False,
        version=1,
        name='test_post'
    )

    assert handler.__name__ == 'handler'
