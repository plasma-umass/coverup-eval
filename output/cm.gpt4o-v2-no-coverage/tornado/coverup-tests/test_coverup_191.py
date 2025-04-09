# file: tornado/escape.py:91-103
# asked: {"lines": [102, 103], "branches": []}
# gained: {"lines": [102, 103], "branches": []}

import pytest
from tornado.escape import url_escape

def test_url_escape_with_plus():
    assert url_escape("hello world") == "hello+world"
    assert url_escape("hello+world") == "hello%2Bworld"
    assert url_escape("hello world", plus=True) == "hello+world"
    assert url_escape("hello world", plus=False) == "hello%20world"
    assert url_escape(b"hello world") == "hello+world"
    assert url_escape(b"hello world", plus=False) == "hello%20world"

def test_url_escape_without_plus():
    assert url_escape("hello world", plus=False) == "hello%20world"
    assert url_escape("hello+world", plus=False) == "hello%2Bworld"
    assert url_escape(b"hello world", plus=False) == "hello%20world"
    assert url_escape(b"hello+world", plus=False) == "hello%2Bworld"

def test_url_escape_bytes():
    assert url_escape(b"hello world") == "hello+world"
    assert url_escape(b"hello+world") == "hello%2Bworld"
    assert url_escape(b"hello world", plus=True) == "hello+world"
    assert url_escape(b"hello world", plus=False) == "hello%20world"
