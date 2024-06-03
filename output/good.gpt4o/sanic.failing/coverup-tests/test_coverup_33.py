# file sanic/exceptions.py:94-102
# lines [94, 95, 99, 100, 101, 102]
# branches []

import pytest
from sanic.exceptions import NotFound

class FileNotFound(NotFound):
    """
    **Status**: 404 Not Found
    """
    def __init__(self, message, path, relative_url):
        super().__init__(message)
        self.path = path
        self.relative_url = relative_url

def test_filenotfound_exception():
    message = "File not found"
    path = "/some/path"
    relative_url = "/relative/url"
    
    exception = FileNotFound(message, path, relative_url)
    
    assert isinstance(exception, FileNotFound)
    assert exception.status_code == 404
    assert exception.path == path
    assert exception.relative_url == relative_url
    assert str(exception) == message
