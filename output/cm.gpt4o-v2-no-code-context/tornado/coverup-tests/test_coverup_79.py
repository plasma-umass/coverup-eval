# file: tornado/auth.py:1170-1173
# asked: {"lines": [1170, 1171, 1172, 1173], "branches": [[1171, 1172], [1171, 1173]]}
# gained: {"lines": [1170, 1171, 1172, 1173], "branches": [[1171, 1172], [1171, 1173]]}

import pytest
from tornado.auth import _oauth_escape

def test_oauth_escape_with_unicode(monkeypatch):
    class MockUnicodeType:
        def __init__(self, value):
            self.value = value

        def encode(self, encoding):
            return self.value.encode(encoding)

    monkeypatch.setattr('tornado.auth.unicode_type', MockUnicodeType)
    input_val = MockUnicodeType("test")
    result = _oauth_escape(input_val)
    assert result == "test"

def test_oauth_escape_with_bytes():
    input_val = b"test"
    result = _oauth_escape(input_val)
    assert result == "test"

def test_oauth_escape_with_str():
    input_val = "test"
    result = _oauth_escape(input_val)
    assert result == "test"
