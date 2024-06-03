# file sanic/response.py:459-496
# lines [459, 461, 462, 463, 464, 485, 486, 487, 491, 492, 493, 494, 495]
# branches ['485->486', '485->491']

import pytest
from sanic.response import stream, StreamingHTTPResponse
from unittest.mock import AsyncMock, patch
import warnings

@pytest.mark.asyncio
async def test_stream_function():
    async def streaming_fn(response):
        await response.write('foo')
        await response.write('bar')

    headers = {"X-Custom-Header": "value"}
    content_type = "text/plain"
    status = 200

    response = stream(streaming_fn, status=status, headers=headers, content_type=content_type)
    
    assert isinstance(response, StreamingHTTPResponse)
    assert response.status == status
    assert response.headers["X-Custom-Header"] == "value"
    assert response.content_type == content_type

@pytest.mark.asyncio
async def test_stream_function_with_chunked_deprecated():
    async def streaming_fn(response):
        await response.write('foo')
        await response.write('bar')

    headers = {"X-Custom-Header": "value"}
    content_type = "text/plain"
    status = 200

    with pytest.warns(DeprecationWarning, match="The chunked argument has been deprecated and will be removed in v21.6"):
        response = stream(streaming_fn, status=status, headers=headers, content_type=content_type, chunked=True)
    
    assert isinstance(response, StreamingHTTPResponse)
    assert response.status == status
    assert response.headers["X-Custom-Header"] == "value"
    assert response.content_type == content_type
