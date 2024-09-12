# file: httpie/utils.py:77-89
# asked: {"lines": [77, 84, 85, 86, 87, 88, 89], "branches": [[85, 0], [85, 86], [87, 88], [87, 89]]}
# gained: {"lines": [77, 84, 85, 86, 87, 88, 89], "branches": [[85, 0], [85, 86], [87, 88], [87, 89]]}

import mimetypes
import pytest

from httpie.utils import get_content_type

def test_get_content_type_known_mime(monkeypatch):
    monkeypatch.setattr(mimetypes, 'guess_type', lambda filename, strict: ('text/plain', None))
    assert get_content_type('test.txt') == 'text/plain'

def test_get_content_type_known_mime_with_encoding(monkeypatch):
    monkeypatch.setattr(mimetypes, 'guess_type', lambda filename, strict: ('text/plain', 'utf-8'))
    assert get_content_type('test.txt') == 'text/plain; charset=utf-8'

def test_get_content_type_unknown_mime(monkeypatch):
    monkeypatch.setattr(mimetypes, 'guess_type', lambda filename, strict: (None, None))
    assert get_content_type('test.unknown') is None
