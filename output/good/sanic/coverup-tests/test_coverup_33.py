# file sanic/response.py:200-204
# lines [200, 201, 202, 203, 204]
# branches ['201->202', '201->204']

import pytest
from sanic.response import StreamingHTTPResponse
from sanic.request import Request
from sanic.server import HttpProtocol
from unittest.mock import MagicMock, Mock

@pytest.mark.asyncio
async def test_streaming_http_response_send():
    # Mock the necessary parts of the response
    request = Mock(spec=Request)
    protocol = Mock(spec=HttpProtocol)
    request.protocol = protocol
    request.app = Mock()
    request.transport = Mock()

    # Define a streaming function to be used
    async def streaming_fn(response):
        await response.write('streaming data')

    # Create a StreamingHTTPResponse instance with the streaming function
    response = StreamingHTTPResponse(streaming_fn)

    # Mock the super().send method
    response.send = MagicMock(side_effect=StreamingHTTPResponse.send)

    # Call the send method which should trigger the streaming function
    await response.send(request)

    # Assert that the streaming function was set to None after being called
    assert response.streaming_fn is None

    # Assert that the super().send method was called
    response.send.assert_called_once()
