# file: tornado/escape.py:214-216
# asked: {"lines": [214, 215, 216], "branches": []}
# gained: {"lines": [214, 215], "branches": []}

import pytest
from tornado.escape import to_unicode

def test_to_unicode_with_none():
    assert to_unicode(None) is None

def test_to_unicode_with_str():
    assert to_unicode("test") == "test"

def test_to_unicode_with_bytes():
    assert to_unicode(b"test") == "test"
