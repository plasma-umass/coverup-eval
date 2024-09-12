# file: tornado/escape.py:173-175
# asked: {"lines": [173, 174, 175], "branches": []}
# gained: {"lines": [173, 174], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_with_bytes():
    input_value = b"test"
    result = utf8(input_value)
    assert result == input_value

def test_utf8_with_str():
    input_value = "test"
    result = utf8(input_value)
    assert result == b"test"

def test_utf8_with_none():
    input_value = None
    result = utf8(input_value)
    assert result is None

def test_utf8_with_int():
    input_value = 123
    with pytest.raises(TypeError):
        utf8(input_value)
