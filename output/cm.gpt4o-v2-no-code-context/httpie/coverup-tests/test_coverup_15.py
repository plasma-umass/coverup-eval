# file: httpie/utils.py:77-89
# asked: {"lines": [77, 84, 85, 86, 87, 88, 89], "branches": [[85, 0], [85, 86], [87, 88], [87, 89]]}
# gained: {"lines": [77, 84, 85, 86, 87, 88, 89], "branches": [[85, 0], [85, 86], [87, 88], [87, 89]]}

import pytest
import mimetypes
from httpie.utils import get_content_type

def test_get_content_type_known_mime(monkeypatch):
    def mock_guess_type(filename, strict):
        return 'text/plain', None
    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)
    
    filename = 'test.txt'
    result = get_content_type(filename)
    assert result == 'text/plain'

def test_get_content_type_known_mime_with_encoding(monkeypatch):
    def mock_guess_type(filename, strict):
        return 'text/plain', 'utf-8'
    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)
    
    filename = 'test.txt'
    result = get_content_type(filename)
    assert result == 'text/plain; charset=utf-8'

def test_get_content_type_unknown_mime(monkeypatch):
    def mock_guess_type(filename, strict):
        return None, None
    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)
    
    filename = 'unknownfile.unknown'
    result = get_content_type(filename)
    assert result is None
