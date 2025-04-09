# file: tornado/escape.py:219-229
# asked: {"lines": [219, 225, 226, 227, 228, 229], "branches": [[225, 226], [225, 227], [227, 228], [227, 229]]}
# gained: {"lines": [219, 225, 226, 227, 228, 229], "branches": [[225, 226], [225, 227], [227, 228], [227, 229]]}

import pytest
from tornado.escape import to_unicode

def test_to_unicode_with_none():
    assert to_unicode(None) is None

def test_to_unicode_with_unicode_string():
    assert to_unicode("test") == "test"

def test_to_unicode_with_bytes():
    assert to_unicode(b"test") == "test"

def test_to_unicode_with_invalid_type():
    with pytest.raises(TypeError, match="Expected bytes, unicode, or None; got"):
        to_unicode(123)

def test_to_unicode_with_empty_bytes():
    assert to_unicode(b"") == ""

def test_to_unicode_with_utf8_bytes():
    assert to_unicode(b"\xe2\x98\x83") == "☃"
