# file sanic/exceptions.py:94-102
# lines [94, 95, 99, 100, 101, 102]
# branches []

import pytest
from sanic.exceptions import FileNotFound

def test_file_not_found_exception():
    message = "File not found"
    path = "/nonexistent/path"
    relative_url = "/nonexistent/url"

    exception = FileNotFound(message, path, relative_url)

    assert exception.status_code == 404
    assert str(exception) == message
    assert exception.path == path
    assert exception.relative_url == relative_url
