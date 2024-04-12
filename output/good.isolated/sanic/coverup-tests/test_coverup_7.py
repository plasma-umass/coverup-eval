# file sanic/response.py:102-122
# lines [102, 104, 105, 113, 114, 115, 116, 117, 118, 119, 120, 122]
# branches ['113->114', '113->115', '115->116', '115->117']

import pytest
from sanic.response import BaseHTTPResponse
from unittest.mock import MagicMock, AsyncMock

@pytest.mark.asyncio
async def test_basehttpresponse_send_no_data_end_stream_none():
    response = BaseHTTPResponse()
    response.stream = MagicMock(send=AsyncMock())

    await response.send()
    response.stream.send.assert_not_called()

@pytest.mark.asyncio
async def test_basehttpresponse_send_with_data():
    response = BaseHTTPResponse()
    response.stream = MagicMock(send=AsyncMock())

    await response.send(data="Test")
    response.stream.send.assert_called_once_with(b"Test", end_stream=None)

@pytest.mark.asyncio
async def test_basehttpresponse_send_with_end_stream():
    response = BaseHTTPResponse()
    response.stream = MagicMock(send=AsyncMock())

    await response.send(end_stream=True)
    response.stream.send.assert_called_once_with(b"", end_stream=True)

@pytest.mark.asyncio
async def test_basehttpresponse_send_with_data_and_end_stream():
    response = BaseHTTPResponse()
    response.stream = MagicMock(send=AsyncMock())

    await response.send(data="Test", end_stream=True)
    response.stream.send.assert_called_once_with(b"Test", end_stream=True)

@pytest.mark.asyncio
async def test_basehttpresponse_send_with_data_bytes():
    response = BaseHTTPResponse()
    response.stream = MagicMock(send=AsyncMock())

    await response.send(data=b"Test")
    response.stream.send.assert_called_once_with(b"Test", end_stream=None)
