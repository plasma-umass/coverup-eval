# file sanic/response.py:349-389
# lines [349, 351, 352, 353, 354, 355, 365, 366, 367, 368, 370, 372, 373, 374, 375, 376, 377, 378, 379, 381, 383, 384, 385, 386, 387, 388]
# branches ['366->367', '366->370', '373->374', '373->381']

import os
import pytest
from sanic.response import HTTPResponse
from sanic import Sanic
from sanic.request import Request
from sanic.app import Sanic
from pathlib import Path
from typing import Union, Optional, Dict
from mimetypes import guess_type

# Assuming Range is a namedtuple or similar simple data structure
from collections import namedtuple
Range = namedtuple('Range', ['start', 'end', 'size', 'total'])

@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("This is a test file.")
    return str(file_path)

@pytest.mark.asyncio
async def test_file_response_with_range(temp_file):
    app = Sanic("test_sanic_app")

    _range = Range(start=0, end=4, size=5, total=5)

    @app.route("/test")
    async def test(request):
        return await file(
            location=temp_file,
            _range=_range
        )

    request, response = await app.asgi_client.get('/test')

    assert response.status == 206
    assert response.body == b"This i"
    assert response.headers["Content-Range"] == "bytes 0-4/5"

@pytest.mark.asyncio
async def test_file_response_without_range(temp_file):
    app = Sanic("test_sanic_app")

    @app.route("/test")
    async def test(request):
        return await file(
            location=temp_file
        )

    request, response = await app.asgi_client.get('/test')

    assert response.status == 200
    assert response.body == b"This is a test file."
    assert "Content-Range" not in response.headers

@pytest.mark.asyncio
async def test_file_response_with_filename(temp_file):
    app = Sanic("test_sanic_app")
    filename = "custom_name.txt"

    @app.route("/test")
    async def test(request):
        return await file(
            location=temp_file,
            filename=filename
        )

    request, response = await app.asgi_client.get('/test')

    assert response.status == 200
    assert response.body == b"This is a test file."
    assert response.headers["Content-Disposition"] == f'attachment; filename="{filename}"'

# The file function to be tested
async def file(
    location: Union[str, Path],
    status: int = 200,
    mime_type: Optional[str] = None,
    headers: Optional[Dict[str, str]] = None,
    filename: Optional[str] = None,
    _range: Optional[Range] = None,
) -> HTTPResponse:
    headers = headers or {}
    if filename:
        headers.setdefault(
            "Content-Disposition", f'attachment; filename="{filename}"'
        )
    filename = filename or os.path.split(location)[-1]

    async with await open_async(location, mode="rb") as f:
        if _range:
            await f.seek(_range.start)
            out_stream = await f.read(_range.size)
            headers[
                "Content-Range"
            ] = f"bytes {_range.start}-{_range.end}/{_range.total}"
            status = 206
        else:
            out_stream = await f.read()

    mime_type = mime_type or guess_type(filename)[0] or "text/plain"
    return HTTPResponse(
        body=out_stream,
        status=status,
        headers=headers,
        content_type=mime_type,
    )

# Mocking open_async to use built-in open function for simplicity
async def open_async(location, mode="rb"):
    return open(location, mode)

# Patching the open_async function in the file function's module
@pytest.fixture(autouse=True)
def mock_open_async(mocker):
    mocker.patch('sanic.response.open_async', new=open_async)
