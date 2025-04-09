# file: tornado/escape.py:204-206
# asked: {"lines": [204, 205, 206], "branches": []}
# gained: {"lines": [204, 205], "branches": []}

import pytest
from tornado.escape import to_unicode

def test_to_unicode_str():
    # This test ensures that the to_unicode function with a str argument is covered
    result = to_unicode("test")
    assert result == "test"

def test_to_unicode_bytes():
    # This test ensures that the to_unicode function with a bytes argument is covered
    result = to_unicode(b"test")
    assert result == "test"

def test_to_unicode_none():
    # This test ensures that the to_unicode function with a None argument is covered
    result = to_unicode(None)
    assert result is None

def test_to_unicode_other():
    # This test ensures that the to_unicode function with a non-str, non-bytes, non-None argument is covered
    with pytest.raises(TypeError):
        to_unicode(123)
