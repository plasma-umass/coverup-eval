# file: tornado/escape.py:209-211
# asked: {"lines": [209, 210, 211], "branches": []}
# gained: {"lines": [209, 210], "branches": []}

import pytest
from tornado.escape import to_unicode

def test_to_unicode_bytes():
    result = to_unicode(b'hello')
    assert result == 'hello'

def test_to_unicode_str():
    result = to_unicode('hello')
    assert result == 'hello'

def test_to_unicode_none():
    result = to_unicode(None)
    assert result is None
