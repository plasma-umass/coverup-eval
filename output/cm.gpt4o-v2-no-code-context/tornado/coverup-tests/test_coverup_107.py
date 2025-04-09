# file: tornado/escape.py:91-103
# asked: {"lines": [91, 102, 103], "branches": []}
# gained: {"lines": [91, 102, 103], "branches": []}

import pytest
from tornado.escape import url_escape

def test_url_escape_with_plus():
    # Test with plus=True (default)
    result = url_escape("hello world")
    assert result == "hello+world"

def test_url_escape_without_plus():
    # Test with plus=False
    result = url_escape("hello world", plus=False)
    assert result == "hello%20world"

def test_url_escape_bytes_with_plus():
    # Test with bytes input and plus=True (default)
    result = url_escape(b"hello world")
    assert result == "hello+world"

def test_url_escape_bytes_without_plus():
    # Test with bytes input and plus=False
    result = url_escape(b"hello world", plus=False)
    assert result == "hello%20world"
