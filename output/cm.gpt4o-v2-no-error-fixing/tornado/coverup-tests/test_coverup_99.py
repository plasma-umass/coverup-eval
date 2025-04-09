# file: tornado/escape.py:178-180
# asked: {"lines": [178, 179, 180], "branches": []}
# gained: {"lines": [178, 179], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_str():
    result = utf8("test")
    assert isinstance(result, bytes)
    assert result == b"test"

def test_utf8_bytes():
    result = utf8(b"test")
    assert isinstance(result, bytes)
    assert result == b"test"
