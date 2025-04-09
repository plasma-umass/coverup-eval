# file sanic/response.py:193-198
# lines [193, 198]
# branches []

import pytest
from sanic.response import StreamingHTTPResponse
from sanic.request import Request
from unittest.mock import MagicMock, Mock

@pytest.mark.asyncio
async def test_streaming_http_response_write():
    # Mock the request and transport
    request = Mock(spec=Request)
    transport = MagicMock()
    request.transport = transport

    # Create instance of StreamingHTTPResponse
    response = StreamingHTTPResponse(content_type='text/plain', request=request)

    # Mock the super().send method
    response.send = MagicMock()

    # Data to write
    data = "Hello, World!"

    # Write data to the streaming response
    await response.write(data)

    # Assert that the send method was called with the correct data
    response.send.assert_called_once_with(response._encode_body(data))

    # Clean up
    del response
