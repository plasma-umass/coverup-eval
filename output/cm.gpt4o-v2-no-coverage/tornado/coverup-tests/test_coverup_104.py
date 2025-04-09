# file: tornado/escape.py:204-206
# asked: {"lines": [204, 205, 206], "branches": []}
# gained: {"lines": [204, 205], "branches": []}

import pytest
from tornado.escape import to_unicode

def test_to_unicode_with_str():
    assert to_unicode("test") == "test"

def test_to_unicode_with_bytes():
    assert to_unicode(b"test") == "test"

def test_to_unicode_with_none():
    assert to_unicode(None) is None
