# file: tornado/escape.py:178-180
# asked: {"lines": [178, 179, 180], "branches": []}
# gained: {"lines": [178, 179], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_overload_str():
    # This test is to ensure that the utf8 function can handle str input correctly
    result = utf8("test")
    assert isinstance(result, bytes)
    assert result == b"test"

def test_utf8_overload_bytes():
    # This test is to ensure that the utf8 function can handle bytes input correctly
    result = utf8(b"test")
    assert isinstance(result, bytes)
    assert result == b"test"

def test_utf8_overload_none():
    # This test is to ensure that the utf8 function can handle None input correctly
    result = utf8(None)
    assert result is None

def test_utf8_overload_invalid_type():
    # This test is to ensure that the utf8 function raises a TypeError for invalid input types
    with pytest.raises(TypeError, match="Expected bytes, unicode, or None; got <class 'int'>"):
        utf8(123)
