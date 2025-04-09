# file sanic/response.py:459-496
# lines [459, 461, 462, 463, 464, 485, 486, 487, 491, 492, 493, 494, 495]
# branches ['485->486', '485->491']

import pytest
from sanic.response import stream, StreamingHTTPResponse
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_stream_function():
    async def streaming_fn(response):
        await response.write('foo')
        await response.write('bar')

    headers = {"X-Custom-Header": "value"}
    response = stream(streaming_fn, status=202, headers=headers, content_type="text/html")

    assert isinstance(response, StreamingHTTPResponse)
    assert response.status == 202
    assert response.headers["X-Custom-Header"] == "value"
    assert response.content_type == "text/html"

@pytest.mark.asyncio
async def test_stream_function_with_chunked_deprecated(mocker):
    async def streaming_fn(response):
        await response.write('foo')
        await response.write('bar')

    mock_warn = mocker.patch("sanic.response.warn")

    headers = {"X-Custom-Header": "value"}
    response = stream(streaming_fn, status=202, headers=headers, content_type="text/html", chunked=True)

    mock_warn.assert_called_once_with(
        "The chunked argument has been deprecated and will be removed in v21.6"
    )
    assert isinstance(response, StreamingHTTPResponse)
    assert response.status == 202
    assert response.headers["X-Custom-Header"] == "value"
    assert response.content_type == "text/html"
