# file sanic/blueprint_group.py:7-56
# lines [7, 8]
# branches []

import pytest
from sanic.blueprints import Blueprint
from sanic import Sanic
from sanic.response import text
from sanic_testing import TestManager

@pytest.fixture
def app():
    app = Sanic("test_app")
    TestManager(app)
    yield app

@pytest.fixture
def client(app):
    return app.asgi_client

@pytest.mark.asyncio
async def test_blueprint_group(app, client):
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = Blueprint.group(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        request.ctx.bp1_middleware = True

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    @bp3.route('/')
    async def bp3_route(request):
        return text('bp3')

    @bp4.route('/<param>')
    async def bp4_route(request, param):
        return text(param)

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        request.ctx.group_middleware = True

    app.blueprint(group)
    app.blueprint(bpg)

    request, response = await client.get('/bp1/')
    assert response.text == 'bp1'
    assert response.status == 200

    request, response = await client.get('/bp2/test_param')
    assert response.text == 'test_param'
    assert response.status == 200

    request, response = await client.get('/api/v1/bp3/')
    assert response.text == 'bp3'
    assert response.status == 200

    request, response = await client.get('/api/v1/bp4/test_param')
    assert response.text == 'test_param'
    assert response.status == 200
