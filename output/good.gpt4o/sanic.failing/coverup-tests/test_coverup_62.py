# file sanic/response.py:128-170
# lines [128, 129, 163]
# branches []

import pytest
from sanic.response import BaseHTTPResponse

@pytest.mark.asyncio
async def test_streaming_http_response():
    class StreamingHTTPResponse(BaseHTTPResponse):
        """
        Old style streaming response where you pass a streaming function:
    
        .. code-block:: python
    
            async def sample_streaming_fn(response):
                await response.write("foo")
                await asyncio.sleep(1)
                await response.write("bar")
                await asyncio.sleep(1)
    
                @app.post("/")
                async def test(request):
                    return stream(sample_streaming_fn)
    
        .. warning::
    
            **Deprecated** and set for removal in v21.6. You can now achieve the
            same functionality without a callback.
    
            .. code-block:: python
    
                @app.post("/")
                async def test(request):
                    response = await request.respond()
                    await response.send("foo", False)
                    await asyncio.sleep(1)
                    await response.send("bar", False)
                    await asyncio.sleep(1)
                    await response.send("", True)
                    return response
    
        """
    
        __slots__ = (
            "streaming_fn",
            "status",
            "content_type",
            "headers",
            "_cookies",
        )

    async def sample_streaming_fn(response):
        await response.write("foo")
        await asyncio.sleep(1)
        await response.write("bar")
        await asyncio.sleep(1)

    response = StreamingHTTPResponse(sample_streaming_fn, status=200, content_type="text/plain")
    assert response.streaming_fn == sample_streaming_fn
    assert response.status == 200
    assert response.content_type == "text/plain"
    assert response.headers == {}
    assert response._cookies == {}
