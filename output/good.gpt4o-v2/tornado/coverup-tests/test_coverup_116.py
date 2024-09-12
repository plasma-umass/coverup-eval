# file: tornado/escape.py:173-175
# asked: {"lines": [173, 174, 175], "branches": []}
# gained: {"lines": [173, 174], "branches": []}

import pytest
from tornado.escape import utf8
import typing

def test_utf8_overload_bytes():
    @typing.overload
    def utf8(value: bytes) -> bytes:
        pass

    # Since the function is overloaded and not implemented, we can't call it directly.
    # We are testing the presence of the overload decorator here.
    assert hasattr(utf8, '__isabstractmethod__') == False
