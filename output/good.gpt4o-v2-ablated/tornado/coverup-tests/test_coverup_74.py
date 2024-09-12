# file: tornado/escape.py:178-180
# asked: {"lines": [178, 179, 180], "branches": []}
# gained: {"lines": [178, 179], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_with_string():
    result = utf8("hello")
    assert isinstance(result, bytes)
    assert result == b"hello"

def test_utf8_with_bytes():
    result = utf8(b"hello")
    assert isinstance(result, bytes)
    assert result == b"hello"

def test_utf8_with_none():
    result = utf8(None)
    assert result is None

def test_utf8_with_integer():
    with pytest.raises(TypeError):
        utf8(123)

def test_utf8_with_list():
    with pytest.raises(TypeError):
        utf8(["hello"])

def test_utf8_with_dict():
    with pytest.raises(TypeError):
        utf8({"key": "value"})
