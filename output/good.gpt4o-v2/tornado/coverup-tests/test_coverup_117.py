# file: tornado/escape.py:178-180
# asked: {"lines": [178, 179, 180], "branches": []}
# gained: {"lines": [178, 179], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_overload_str():
    # This test is to ensure the overload for str type is covered
    result = utf8("test")
    assert isinstance(result, bytes)
    assert result == b"test"

def test_utf8_overload_bytes():
    # This test is to ensure the overload for bytes type is covered
    result = utf8(b"test")
    assert isinstance(result, bytes)
    assert result == b"test"

def test_utf8_overload_none():
    # This test is to ensure the overload for None type is covered
    result = utf8(None)
    assert result is None
