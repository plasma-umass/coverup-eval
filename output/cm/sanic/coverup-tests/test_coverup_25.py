# file sanic/response.py:392-456
# lines [392, 394, 395, 396, 397, 398, 399, 400, 412, 413, 414, 418, 419, 420, 421, 423, 424, 425, 426, 427, 428, 430, 431, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 445, 446, 447, 448, 449, 451, 452, 453, 454, 455]
# branches ['412->413', '412->418', '419->420', '419->423', '425->426', '425->433', '435->436', '435->445', '438->exit', '438->439', '440->441', '440->442', '445->446', '447->448', '447->449']

import os
import pytest
from sanic.response import file_stream, StreamingHTTPResponse
from sanic.request import Request
from sanic.server import HttpProtocol
from unittest.mock import MagicMock
from pathlib import Path
from typing import Union
from tempfile import NamedTemporaryFile

@pytest.mark.asyncio
async def test_file_stream_with_range_and_filename(mocker):
    # Setup temporary file
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b'Hello World')
        tmp_path = tmp.name

    # Mock request and protocol
    request = mocker.create_autospec(Request)
    protocol = mocker.create_autospec(HttpProtocol)
    request.protocol = protocol
    request.app = mocker.MagicMock()
    request.transport = mocker.MagicMock()

    # Define a range object
    class Range:
        def __init__(self, start, end, total):
            self.start = start
            self.end = end
            self.total = total
            self.size = end - start + 1

    _range = Range(0, 4, 11)  # Range for 'Hello'

    # Call the file_stream function
    response = await file_stream(
        location=tmp_path,
        filename='greeting.txt',
        _range=_range
    )

    # Assertions to verify the response
    assert isinstance(response, StreamingHTTPResponse)
    assert response.status == 206
    assert response.headers['Content-Disposition'] == 'attachment; filename="greeting.txt"'
    assert response.headers['Content-Range'] == 'bytes 0-4/11'
    assert response.content_type == 'text/plain'

    # Cleanup temporary file
    os.unlink(tmp_path)

@pytest.mark.asyncio
async def test_file_stream_deprecated_chunked_argument(mocker):
    # Setup temporary file
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b'Hello World')
        tmp_path = tmp.name

    # Mock request and protocol
    request = mocker.create_autospec(Request)
    protocol = mocker.create_autospec(HttpProtocol)
    request.protocol = protocol
    request.app = mocker.MagicMock()
    request.transport = mocker.MagicMock()

    # Mock the warning to check if it's called
    mocker.patch('sanic.response.warn')

    # Call the file_stream function with deprecated chunked argument
    response = await file_stream(
        location=tmp_path,
        chunked=True
    )

    # Assertions to verify the response and the warning
    assert isinstance(response, StreamingHTTPResponse)
    from sanic.response import warn
    warn.assert_called_once_with(
        "The chunked argument has been deprecated and will be removed in v21.6"
    )

    # Cleanup temporary file
    os.unlink(tmp_path)
