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
async def test_file_response_with_range(mocker):
    # Mock the open_async function
    mock_open_async = mocker.patch("sanic.response.open_async", mock_open(read_data=b"test data"))
    mock_file = mock_open_async.return_value.__aenter__.return_value
    mock_file.read = mocker.AsyncMock(return_value=b"test data")
    mock_file.seek = mocker.AsyncMock()

    # Define the range
    class Range:
        start = 0
        end = 3
        size = 4
        total = 8

    # Call the file function
    response = await file("dummy_path", _range=Range)

    # Assertions
    assert response.status == 206
    assert response.body == b"test data"
    assert response.headers["Content-Range"] == "bytes 0-3/8"
    assert response.content_type == "text/plain"

@pytest.mark.asyncio
async def test_file_response_without_range(mocker):
    # Mock the open_async function
    mock_open_async = mocker.patch("sanic.response.open_async", mock_open(read_data=b"test data"))
    mock_file = mock_open_async.return_value.__aenter__.return_value
    mock_file.read = mocker.AsyncMock(return_value=b"test data")

    # Call the file function
    response = await file("dummy_path")

    # Assertions
    assert response.status == 200
    assert response.body == b"test data"
    assert response.content_type == "text/plain"

@pytest.mark.asyncio
async def test_file_response_with_filename(mocker):
    # Mock the open_async function
    mock_open_async = mocker.patch("sanic.response.open_async", mock_open(read_data=b"test data"))
    mock_file = mock_open_async.return_value.__aenter__.return_value
    mock_file.read = mocker.AsyncMock(return_value=b"test data")

    # Call the file function
    response = await file("dummy_path", filename="test.txt")

    # Assertions
    assert response.status == 200
    assert response.body == b"test data"
    assert response.headers["Content-Disposition"] == 'attachment; filename="test.txt"'
    assert response.content_type == "text/plain"
