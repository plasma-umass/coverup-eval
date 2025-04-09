# file: tornado/escape.py:173-175
# asked: {"lines": [173, 174, 175], "branches": []}
# gained: {"lines": [173, 174], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_bytes_overload():
    # This test is to ensure that the bytes overload for utf8 is covered
    result = utf8(b"test")
    assert result == b"test"

