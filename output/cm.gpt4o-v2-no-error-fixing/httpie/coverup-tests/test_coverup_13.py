# file: httpie/utils.py:77-89
# asked: {"lines": [77, 84, 85, 86, 87, 88, 89], "branches": [[85, 0], [85, 86], [87, 88], [87, 89]]}
# gained: {"lines": [77, 84, 85, 86, 87, 88, 89], "branches": [[85, 0], [85, 86], [87, 88], [87, 89]]}

import pytest
import mimetypes
from httpie.utils import get_content_type

def test_get_content_type_known_mime():
    filename = 'example.txt'
    expected_mime = 'text/plain'
    result = get_content_type(filename)
    assert result == expected_mime

def test_get_content_type_known_mime_with_encoding(monkeypatch):
    filename = 'example.gz'
    expected_mime = 'application/gzip; charset=gzip'

    def mock_guess_type(name, strict):
        return ('application/gzip', 'gzip')

    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)
    result = get_content_type(filename)
    assert result == expected_mime

def test_get_content_type_unknown_mime(monkeypatch):
    filename = 'example.unknown'
    
    def mock_guess_type(name, strict):
        return (None, None)

    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)
    result = get_content_type(filename)
    assert result is None
