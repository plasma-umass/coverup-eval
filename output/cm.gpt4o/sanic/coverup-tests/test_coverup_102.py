# file sanic/exceptions.py:94-102
# lines [100, 101, 102]
# branches []

import pytest
from sanic.exceptions import NotFound, FileNotFound

def test_filenotfound_initialization():
    message = "File not found"
    path = "/some/path"
    relative_url = "/relative/url"
    
    exception = FileNotFound(message, path, relative_url)
    
    assert exception.args[0] == message
    assert exception.path == path
    assert exception.relative_url == relative_url
