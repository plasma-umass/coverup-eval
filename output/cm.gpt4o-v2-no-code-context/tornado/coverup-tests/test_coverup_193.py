# file: tornado/log.py:74-78
# asked: {"lines": [77, 78], "branches": []}
# gained: {"lines": [77, 78], "branches": []}

import pytest
from tornado.log import _safe_unicode

def test_safe_unicode_with_unicode_decode_error(monkeypatch):
    class MockUnicodeDecodeError(UnicodeDecodeError):
        def __init__(self):
            pass

    def mock_unicode(s):
        raise MockUnicodeDecodeError()

    monkeypatch.setattr('tornado.log._unicode', mock_unicode)
    
    result = _safe_unicode(b'\x80')
    assert result == "b'\\x80'"

def test_safe_unicode_without_error(monkeypatch):
    def mock_unicode(s):
        return str(s)

    monkeypatch.setattr('tornado.log._unicode', mock_unicode)
    
    result = _safe_unicode('test')
    assert result == 'test'
