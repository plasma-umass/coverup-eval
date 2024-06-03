# file sanic/response.py:392-456
# lines [392, 394, 395, 396, 397, 398, 399, 400, 412, 413, 414, 418, 419, 420, 421, 423, 424, 425, 426, 427, 428, 430, 431, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 445, 446, 447, 448, 449, 451, 452, 453, 454, 455]
# branches ['412->413', '412->418', '419->420', '419->423', '425->426', '425->433', '435->436', '435->445', '438->exit', '438->439', '440->441', '440->442', '445->446', '447->448', '447->449']

import pytest
from sanic.response import file_stream
from sanic import Sanic
from sanic.request import Request
from sanic.response import StreamingHTTPResponse
from unittest.mock import patch, mock_open
from pathlib import Path
import os

@pytest.mark.asyncio
async def test_file_stream(mocker):
    app = Sanic("test_sanic")
    location = "test_file.txt"
    content = b"Hello, world!"
    chunk_size = 5
    mime_type = "text/plain"
    headers = {"Custom-Header": "value"}
    filename = "download.txt"
    _range = None

    # Mock the open_async function
    mocker.patch("sanic.response.open_async", mock_open(read_data=content))

    # Create a mock request
    request, response = Request(b"/", {}, None, None, None, None), None

    # Test the file_stream function
    response = await file_stream(
        location=location,
        chunk_size=chunk_size,
        mime_type=mime_type,
        headers=headers,
        filename=filename,
        _range=_range,
    )

    assert isinstance(response, StreamingHTTPResponse)
    assert response.status == 200
    assert response.headers["Content-Disposition"] == f'attachment; filename="{filename}"'
    assert response.headers["Custom-Header"] == "value"
    assert response.content_type == mime_type

    # Test the streaming function
    streaming_fn = response.streaming_fn
    mock_response = mocker.Mock()
    await streaming_fn(mock_response)

    # Check that the file was read in chunks
    mock_response.write.assert_any_call(content[:chunk_size])
    mock_response.write.assert_any_call(content[chunk_size:chunk_size*2])

    # Clean up
    if os.path.exists(location):
        os.remove(location)
