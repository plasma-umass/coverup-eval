# file sanic/response.py:128-170
# lines [128, 129, 163]
# branches []

import asyncio
import pytest
from sanic import Sanic, response
from sanic.request import Request

@pytest.mark.asyncio
async def test_streaming_http_response(mocker):
    app = Sanic("test_sanic_app")

    async def sample_streaming_fn(response):
        await response.write("foo")
        await asyncio.sleep(0.1)
        await response.write("bar")

    @app.post("/")
    async def test(request: Request):
        return response.stream(sample_streaming_fn)

    request, response = await app.asgi_client.post("/")
    assert response.status == 200
    assert "foo" in response.body.decode()
    assert "bar" in response.body.decode()

    # Check if the response is indeed a StreamingHTTPResponse
    assert isinstance(response, response.StreamingHTTPResponse)
