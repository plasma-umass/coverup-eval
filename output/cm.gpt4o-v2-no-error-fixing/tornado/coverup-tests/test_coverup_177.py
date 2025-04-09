# file: tornado/log.py:74-78
# asked: {"lines": [77, 78], "branches": []}
# gained: {"lines": [77, 78], "branches": []}

import pytest
from tornado.log import _safe_unicode

def test_safe_unicode_with_unicode_decode_error(monkeypatch):
    class MockUnicodeDecodeError(Exception):
        pass

    def mock_unicode(s):
        raise MockUnicodeDecodeError()

    monkeypatch.setattr('tornado.escape._unicode', mock_unicode)

    result = _safe_unicode(b'\x80abc')
    assert result == "b'\\x80abc'"
