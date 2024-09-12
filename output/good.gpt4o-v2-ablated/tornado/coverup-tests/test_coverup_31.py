# file: tornado/escape.py:188-198
# asked: {"lines": [188, 194, 195, 196, 197, 198], "branches": [[194, 195], [194, 196], [196, 197], [196, 198]]}
# gained: {"lines": [188, 194, 195, 196, 197, 198], "branches": [[194, 195], [194, 196], [196, 197], [196, 198]]}

import pytest
from tornado.escape import utf8

def test_utf8_with_bytes():
    assert utf8(b"test") == b"test"

def test_utf8_with_none():
    assert utf8(None) is None

def test_utf8_with_unicode():
    assert utf8("test") == b"test"

def test_utf8_with_invalid_type():
    with pytest.raises(TypeError, match="Expected bytes, unicode, or None; got <class 'int'>"):
        utf8(123)
