# file sanic/response.py:193-198
# lines [193, 198]
# branches []

import pytest
from sanic.response import BaseHTTPResponse

class StreamingHTTPResponse(BaseHTTPResponse):
    async def write(self, data):
        """Writes a chunk of data to the streaming response.

        :param data: str or bytes-ish data to be written.
        """
        await super().send(self._encode_body(data))

@pytest.mark.asyncio
async def test_streaming_http_response_write(mocker):
    # Mock the send method of BaseHTTPResponse
    mock_send = mocker.patch.object(BaseHTTPResponse, 'send', return_value=None)
    
    # Create an instance of StreamingHTTPResponse
    response = StreamingHTTPResponse()
    
    # Mock the _encode_body method to return the data as is
    mocker.patch.object(response, '_encode_body', side_effect=lambda x: x)
    
    # Test data
    test_data = b"test data"
    
    # Call the write method
    await response.write(test_data)
    
    # Assert that the send method was called with the correct data
    mock_send.assert_called_once_with(test_data)
