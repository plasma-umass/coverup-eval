# file sanic/response.py:200-204
# lines [200, 201, 202, 203, 204]
# branches ['201->202', '201->204']

import pytest
from sanic.response import BaseHTTPResponse

class MockStreamingHTTPResponse(BaseHTTPResponse):
    def __init__(self, streaming_fn=None):
        super().__init__()
        self.streaming_fn = streaming_fn

    async def send(self, *args, **kwargs):
        if self.streaming_fn is not None:
            await self.streaming_fn(self)
            self.streaming_fn = None
        await super().send(*args, **kwargs)

@pytest.mark.asyncio
async def test_streaming_http_response_send(mocker):
    async def mock_streaming_fn(response):
        response.body = b"streamed data"

    mock_response = MockStreamingHTTPResponse(streaming_fn=mock_streaming_fn)
    mock_super_send = mocker.patch.object(BaseHTTPResponse, 'send', return_value=None)

    await mock_response.send()

    assert mock_response.body == b"streamed data"
    assert mock_response.streaming_fn is None
    mock_super_send.assert_called_once()
