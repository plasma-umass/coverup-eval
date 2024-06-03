# file sanic/response.py:349-389
# lines [349, 351, 352, 353, 354, 355, 365, 366, 367, 368, 370, 372, 373, 374, 375, 376, 377, 378, 379, 381, 383, 384, 385, 386, 387, 388]
# branches ['366->367', '366->370', '373->374', '373->381']

import pytest
from sanic.response import file
from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse
from unittest.mock import patch, mock_open
from pathlib import Path
import os

@pytest.mark.asyncio
async def test_file_response_with_range():
    location = "test_file.txt"
    content = b"Hello, world!"
    _range = Range(start=0, end=4, size=5, total=len(content))

    with patch("sanic.response.open_async", mock_open(read_data=content)) as mock_file:
        response = await file(location, _range=_range)

    mock_file.assert_called_once_with(location, mode="rb")
    assert response.status == 206
    assert response.body == content[:5]
    assert response.headers["Content-Range"] == "bytes 0-4/13"
    assert response.content_type == "text/plain"

@pytest.mark.asyncio
async def test_file_response_with_filename():
    location = "test_file.txt"
    content = b"Hello, world!"
    filename = "download.txt"

    with patch("sanic.response.open_async", mock_open(read_data=content)) as mock_file:
        response = await file(location, filename=filename)

    mock_file.assert_called_once_with(location, mode="rb")
    assert response.status == 200
    assert response.body == content
    assert response.headers["Content-Disposition"] == f'attachment; filename="{filename}"'
    assert response.content_type == "text/plain"

@pytest.mark.asyncio
async def test_file_response_with_mime_type():
    location = "test_file.txt"
    content = b"Hello, world!"
    mime_type = "application/octet-stream"

    with patch("sanic.response.open_async", mock_open(read_data=content)) as mock_file:
        response = await file(location, mime_type=mime_type)

    mock_file.assert_called_once_with(location, mode="rb")
    assert response.status == 200
    assert response.body == content
    assert response.content_type == mime_type

@pytest.mark.asyncio
async def test_file_response_with_headers():
    location = "test_file.txt"
    content = b"Hello, world!"
    headers = {"X-Custom-Header": "value"}

    with patch("sanic.response.open_async", mock_open(read_data=content)) as mock_file:
        response = await file(location, headers=headers)

    mock_file.assert_called_once_with(location, mode="rb")
    assert response.status == 200
    assert response.body == content
    assert response.headers["X-Custom-Header"] == "value"
    assert response.content_type == "text/plain"

class Range:
    def __init__(self, start, end, size, total):
        self.start = start
        self.end = end
        self.size = size
        self.total = total
