# file: tornado/escape.py:178-180
# asked: {"lines": [178, 179, 180], "branches": []}
# gained: {"lines": [178, 179], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_with_str():
    result = utf8("hello")
    assert result == b"hello"

def test_utf8_with_bytes():
    result = utf8(b"hello")
    assert result == b"hello"

def test_utf8_with_none():
    result = utf8(None)
    assert result is None
