# file: tornado/escape.py:91-103
# asked: {"lines": [91, 102, 103], "branches": []}
# gained: {"lines": [91, 102, 103], "branches": []}

import pytest
from tornado.escape import url_escape

def test_url_escape_with_plus():
    assert url_escape("hello world", plus=True) == "hello+world"
    assert url_escape("hello+world", plus=True) == "hello%2Bworld"
    assert url_escape("hello world", plus=False) == "hello%20world"
    assert url_escape("hello%20world", plus=False) == "hello%2520world"

def test_url_escape_bytes():
    assert url_escape(b"hello world", plus=True) == "hello+world"
    assert url_escape(b"hello+world", plus=True) == "hello%2Bworld"
    assert url_escape(b"hello world", plus=False) == "hello%20world"
    assert url_escape(b"hello%20world", plus=False) == "hello%2520world"
