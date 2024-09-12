# file: tornado/escape.py:209-211
# asked: {"lines": [209, 210, 211], "branches": []}
# gained: {"lines": [209, 210], "branches": []}

import pytest
from tornado.escape import to_unicode

def test_to_unicode_with_bytes():
    result = to_unicode(b'hello')
    assert result == 'hello'

def test_to_unicode_with_empty_bytes():
    result = to_unicode(b'')
    assert result == ''

def test_to_unicode_with_non_ascii_bytes():
    result = to_unicode(b'\xe2\x98\x83')
    assert result == '☃'

def test_to_unicode_with_invalid_bytes():
    with pytest.raises(UnicodeDecodeError):
        to_unicode(b'\x80\x81')

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up or reset any state if necessary
    yield
    # Perform any necessary cleanup after each test
